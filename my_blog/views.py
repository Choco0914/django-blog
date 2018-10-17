from django.shortcuts import render, get_object_or_404
from django.http import HttpResponseRedirect, Http404
from django.urls import reverse

from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.db.models import Q

from .models import Topic, Content, Comment
from .forms import TopicForm, ContentForm, CommentForm

def check_topic_owner(request, topic):
    """주제에 연결된 사용자가 현재 로그인된 사용자와 일치하는지 확인한다"""
    if topic.owner != request.user:
        raise Http404

def index(request):
    """블로그 홈페이지"""
    return render(request, 'my_blog/index.html')

def _get_topics_For_user(user):
    """유저가 접근할수 있는 쿼리셋을 돌려준다"""
    q = Q(public=True)
    # If django < 1.10 you want "user.is_authenticated()" (with parens)
    if user.is_authenticated:
        # Adds user's own private topics to the query
        q = q | Q(public=False, owner=user)

    return Topic.objects.filter(q)

# 주제
def topics(request):
    """주제를 나타내는 page"""
    topics = _get_topics_For_user(request.user).order_by('date_added')
    form = TopicForm()
    context = {'topics': topics, 'form':form}
    return render(request, 'my_blog/topics.html', context)

def topic(request, topic_id):
    """주제 하나와 연결된 모든 내용을 표시한다"""
    topics = _get_topics_For_user(request.user)
    topic = get_object_or_404(topics, id=topic_id)
    form = TopicForm()
    # Here we're passing the filtered queryset, so
    # if the topic "topic_id" is private and the user is either
    # anonyous or not the topic owner, it will raise a 404
    if topic.owner == request.user:
        contents = topic.content_set.order_by('-date_added')
        context = {'topic':topic, 'contents':contents, 'form': form}
        return render(request, 'my_blog/topic.html', context)
    else:
        contents = topic.content_set.order_by('-date_added')
        context = {'topic': topic, 'contents': contents, 'form': form}
    return render(request, 'my_blog/public_topic.html', context)

@login_required
def new_topic(request):
    """새로운 주제를 추가한다."""
    if request.method != 'POST':
        # 들어온 데이터가 없을 때는 새폼을 만든다.
        form = TopicForm()
    else:
        # POST 데이터를 받아서 처리한다.
        form = TopicForm(request.POST)
        if form.is_valid():
            new_topic = form.save(commit=False)
            new_topic.owner = request.user
            new_topic.save()
            return HttpResponseRedirect(reverse('my_blog:topics'))
    context = {'form': form}
    return render(request, 'my_blog/new_topic.html', context)

@login_required
def delete_topic(request, topic_id):
    """주제를 삭제해준다."""
    topic = get_object_or_404(Topic, id=topic_id)
    check_user = check_topic_owner(request, topic)

    topic.delete()
    return HttpResponseRedirect(reverse('my_blog:topics'))

# 내용
def read_content(request, content_id):
    """내용을 자세히 보여준다."""
    content = get_object_or_404(Content, id=content_id)
    topic = content.topic
    form = CommentForm()
    topic_id = topic.id
    topics = _get_topics_For_user(request.user)
    topic_get = get_object_or_404(topics, id=topic_id)
    for selected_content in topic_get.content_set.all():
        if content == selected_content:
            content = selected_content

    context = {'content':content, 'topic':topic,}
    return render(request, 'my_blog/read_content.html', context)

@login_required
def new_content(request, topic_id):
    """새로운 내용을 추가한다"""
    topic = Topic.objects.get(id=topic_id)

    if request.method != 'POST':
        # 전송된 데이터가 없으므로 빈 폼을 만든다.
        form = ContentForm()
    else:
        # 받은 POST 데이터를 처리한다.
        form = ContentForm(data=request.POST)
        if form.is_valid():
            new_content = form.save(commit=False)
            new_content.topic = topic
            new_content.owner = request.user
            new_content.save()
            return HttpResponseRedirect(reverse('my_blog:topic',
            args=[topic_id]))
    context = {'topic':topic, 'form':form}
    return render(request, 'my_blog/new_content.html', context)

@login_required
def edit_content(request, content_id):
    """내용을 수정해준다."""
    content = Content.objects.get(id=content_id)
    topic = content.topic
    check = check_topic_owner(request, topic)

    if request.method != 'POST':
        # 첫 요청이므로 폼을 현재 텍스트로 채워준다.
        form = ContentForm(instance=content)
    else:
        # POST 데이터를 받았으므로 받은 데이터를 처리한다.
        form = ContentForm(instance=content, data=request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('my_blog:topic',
                                            args=[topic.id]))

    context= {'content':content, 'topic':topic, 'form': form}
    return render(request, 'my_blog/edit_content.html', context)

@login_required
def delete_content(request, content_id):
    """내용를 삭제해준다."""
    content = get_object_or_404(Content, id=content_id)
    topic = content.topic
    check_user = check_topic_owner(request, topic)

    content.delete()
    return HttpResponseRedirect(reverse('my_blog:topic', args=[topic.id]))

# 댓글
@login_required
def new_comment(request, content_id):
    """새로운 댓글을 달게 한다."""
    content = get_object_or_404(Content, id=content_id)
    topic = content.topic

    if request.method != "POST":
        form = CommentForm()
    else:
        form = CommentForm(data=request.POST)
        if form.is_valid():
            new_comment = form.save(commit=False)
            new_comment.content = content
            new_comment.author = request.user
            new_comment.save()
            return HttpResponseRedirect(reverse('my_blog:read_content',
                                        args=[content_id]))

    context = {'content':content, 'topic':topic, 'form':form, }
    return render(request, 'my_blog/add_comment.html',
            context)

def delete_comment(request, comment_id):
    """댓글을 삭제한다."""
    comment = get_object_or_404(Comment, id=comment_id)
    content = comment.content
    # 댓글의 유저를 확인한다.
    if comment.author != request.user:
        raise Http404

    comment.delete()
    return HttpResponseRedirect(reverse('my_blog:read_content',
                                    args=[content.id]))
