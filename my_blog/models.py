from django.db import models

class Topic(models.Model):
    """Topic은 사용자가 블로그에서 다루는 주제"""
    text = models.CharField(max_length=200)
    date_added = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        """모델에 관한 정보를 문자열 형태로 반환한다."""
        return self.text
