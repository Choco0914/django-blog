"""users 앱의 URL 패턴을 정의하는 파일"""

from django.urls import re_path
from django.contrib.auth import views as auth_views

from . import views

app_name = 'users'

urlpatterns = [
    # 로그인 페이지
    re_path(r'^login/$',
    auth_views.LoginView.as_view(template_name='users/login.html'),
    name = 'login'),

    # 로그아웃 페이지
    re_path(r'^logout/$',views.logout_view, name='logout'),

    # 유저 등록 페이지
    re_path(r'^register/$', views.register, name='register'),

]
