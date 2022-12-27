from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.
class User(AbstractUser):
    # 'self' 자기 자신 참고 -> 대댓글 구현할 때 사용함. 이떄의 댓글 자체 N:1 / sysmmetrical=True면 맞팔되어버림
    followings = models.ManyToManyField('self', symmetrical=False, related_name='followers')
