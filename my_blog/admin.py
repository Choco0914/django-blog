from django.contrib import admin

from .models import Topic, Content, Comment

admin.site.register(Topic)
admin.site.register(Content)
admin.site.register(Comment)
