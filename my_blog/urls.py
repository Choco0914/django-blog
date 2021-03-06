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
    # 주제를 삭제하는 Url
    re_path(r'^topics/(?:page-(?P<topic_id>\d+)/delete_topic/)?$',
    views.delete_topic, name='delete_topic'),

    # Content page
    # 내용을 자세히 보여주는 페이지
    re_path(r'^contents/(?:page-(?P<content_id>\d+)/read_content/)?$',
    views.read_content, name='read_content'),
    # 새 내용 추가 페이지
    re_path(r'^new_topic/(?:page-(?P<topic_id>\d+)/)?$',
    views.new_content, name='new_content'),
    # 내용 수정 페이지
    re_path(r'^edit_content/(?:page-(?P<content_id>\d+)/)?$',
    views.edit_content, name='edit_content'),
    # 내용 삭제 Url
    re_path(r'^contents/(?:page-(?P<content_id>\d+)/delete_content/)?$',
    views.delete_content, name='delete_content'),

    # Comment page
    # 새로운 댓글을 추가하는 페이지
    re_path(r'^comment/(?:page-(?P<content_id>\d+)/new_comment/)?$',
    views.new_comment, name='new_comment'),
    # 댓글을 삭제하는 Url
    re_path(r'^comment/(?:page-(?P<comment_id>\d+)/delete_comment/)?$',
    views.delete_comment, name='delete_comment'),

    # User
    # 유저의 프로필을 나타내는 페이지
    re_path(r'^profile/(?:page-(?P<user_id>\d+)/)?$', views.profile,
        name='profile'),
    re_path(r'^profile/(?:page-(?P<user_id>\d+)/delete_user/)?$',
        views.delete_user, name='delete_user')
]
