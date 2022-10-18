from django.db import models
from apps.utils.models import Base
from django.contrib.auth.models import User


class Profile(Base):
    class Meta:
        verbose_name = '用户属性'
        verbose_name_plural = '用户属性'

    user = models.OneToOneField(User, on_delete=models.CASCADE)

    def __str__(self):
        return "用户{}个人属性".format(self.user)

