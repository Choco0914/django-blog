from django.db import models
from django.contrib.auth.models import User

class Topic(models.Model):
    """Topic은 사용자가 블로그에서 다루는 주제"""
    text = models.CharField(max_length=200)
    date_added = models.DateTimeField(auto_now_add=True)
    owner = models.ForeignKey(User, on_delete= models.CASCADE)

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
        return self.text[:50] + "..."
