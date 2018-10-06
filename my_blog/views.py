from django.shortcuts import render
from django.http import HttpResponseRedirect, Http404
from django.urls import reverse
from django.contrib.auth.decorators import login_required

from .models import Topic ,Content
from .forms import TopicForm, ContentForm

def index(request):
    """블로그 홈페이지"""
    return render(request, 'my_blog/index.html')

@login_required
def topics(request):
    """주제를 나타내는 page"""
    topics = Topic.objects.filter(owner=request.user).order_by('date_added')
    context = {'topics': topics}
    return render(request, 'my_blog/topics.html', context)

@login_required
def topic(request, topic_id):
    """주제 하나와 연결된 모든 내용을 표시한다"""
    topic = Topic.objects.get(id=topic_id)
    # 주제가 현재 사용자의 것인지 확인한다.
    check = check_topic_owner(request, topic)

    contents = topic.content_set.order_by('-date_added')
    context = {'topic':topic, 'contents': contents}
    return render(request, 'my_blog/topic.html', context)

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

def check_topic_owner(request, topic):
    """주제에 연결된 사용자가 현재 로그인된 사용자와 일치하는지 확인한다"""
    if topic.owner != request.user:
        raise Http404
