from django.contrib import admin
from django.urls import path, re_path, include

app_namespace = 'my_blog'

urlpatterns = [
    re_path(r'^admin/', admin.site.urls),
    re_path(r'', include(('my_blog.urls', app_namespace), namespace=None)),
]
