from django.db import models
from django.contrib.auth.models import User

class Profile(models.Model):
    "Profile 정의 하는 모델"
    user = models.OneToOneField(User, related_name='profile',
    on_delete= models.CASCADE)
    activation_key = models.CharField(max_length=40)
    key_expries = models.DateTimeField()
