from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, re_path, include

urlpatterns = [
    re_path(r'^admin/', admin.site.urls),

    # my_blog app url
    re_path(r'', include(('my_blog.urls', 'my_blog'), namespace=None)),

    # users app url
    re_path(r'^users/', include(('users.urls', 'users'), namespace=None)),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
