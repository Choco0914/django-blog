"""my_blog의 URL의 패턴을 정의한다."""

from django.urls import re_path

from . import views

urlpatterns =[
    # Homepage
    re_path(r'$', views.index, name = 'index')
]
