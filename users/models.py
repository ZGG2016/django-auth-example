from django.db import models
from django.contrib.auth.models import AbstractUser


# TODO 继承 AbstractUser 拓展用户模型
class User(AbstractUser):
    nickname = models.CharField(max_length=50, blank=True)

    class Meta(AbstractUser.Meta):
        pass


# TODO 使用 Profile 模式拓展用户模型
# class Profile(models.Model):
#     nickname = models.CharField(max_length=50, blank=True)
#     user = models.OneToOneField(User)
