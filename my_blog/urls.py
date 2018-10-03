"""my_blog의 URL의 패턴을 정의한다."""

from django.urls import re_path

from . import views

urlpatterns =[
    # Homepage
    re_path(r'^$', views.index, name = 'index'),

    #Topic page
    re_path(r'^topics/$', views.topics, name='topics'),

    #주제 하나에 대한 세부사항 페이지
    re_path(r'^topics/(?:page-(?P<topic_id>\d+)/)?$', views.topic, name='topic' ),
]
