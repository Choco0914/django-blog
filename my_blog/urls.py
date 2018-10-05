"""my_blog의 URL의 패턴을 정의한다."""

from django.urls import re_path

from . import views

urlpatterns =[
    # Homepage
    re_path(r'^$', views.index, name = 'index'),

    #Topic page
    re_path(r'^topics/$', views.topics, name='topics'),

    #주제 하나에 대한 세부사항 페이지
    re_path(r'^topics/(?:page-(?P<topic_id>\d+)/)?$',
    views.topic, name='topic' ),

    # 새 주제를 추가하는 페이지
    re_path(r'^new_topic/$', views.new_topic, name='new_topic'),

    # 새 내용 추가 페이지
    re_path(r'^new_topic/(?:page-(?P<topic_id>\d+)/)?$',
    views.new_content, name='new_content'),

    # 내용 수정 페이지
    re_path(r'^edit_content/(?:page-(?P<content_id>\d+)/)?$',
    views.edit_content, name='edit_content'),
]
