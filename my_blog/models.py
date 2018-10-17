from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone

class Topic(models.Model):
    """Topic은 사용자가 블로그에서 다루는 주제"""
    text = models.CharField(max_length=200)
    date_added = models.DateTimeField(auto_now_add=True)
    owner = models.ForeignKey(User, on_delete= models.CASCADE)
    public = models.BooleanField(default=False)

    def __str__(self):
        """모델에 관한 정보를 문자열 형태로 반환한다."""
        return self.text

class Content(models.Model):
    """Topic의 내용이 들어간다"""
    topic = models.ForeignKey(Topic, on_delete = models.CASCADE)
    text = models.TextField()
    date_added = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name_plural = 'contents'

    def __str__(self):
        """모델에 관한 정보를 문자열 형태로 반환한다."""
        if self.text[:] > self.text[:50]:
            return self.text[:50] + "..."
        else:
            return self.text[:]

class Comment(models.Model):
    """댓글의 모델을 정의한다"""
    content = models.ForeignKey(Content, related_name='comments',
                            on_delete = models.CASCADE)
    text = models.TextField()
    author = models.ForeignKey(User, on_delete = models.CASCADE)
    created_date = models.DateTimeField(auto_now_add=True)
    approved_comment = models.BooleanField(default=False)

    def approve(self):
        """댓글을 승인한다"""
        self.approved_comment = True
        self.save()

    def __str__(self):
        """모델에 관한 정보를 문자열 형태로 반환한다."""
        return self.text
