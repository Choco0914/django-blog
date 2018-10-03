from django.shortcuts import render
from .models import Topic

def index(request):
    """블로그 홈페이지"""
    return render(request, 'my_blog/index.html')

def topics(request):
    """주제를 나타내는 page"""
    topics = Topic.objects.order_by('date_added')
    context = {'topics': topics}
    return render(request, 'my_blog/topics.html', context)

def topic(request, topic_id):
    """주제 하나와 연결된 모든 내용을 표시한다"""
    topic = Topic.objects.get(id=topic_id)
    contents = topic.content_set.order_by('-date_added')
    context = {'topic':topic, 'contents': contents}
    return render(request, 'my_blog/topic.html', context)
