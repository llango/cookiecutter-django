#!coding:utf-8
from __future__ import unicode_literals

from django.db import models
from django.utils import timezone


class Base(models.Model):
    """项目中所有其他模型的模型库。"""

    class Meta:
        abstract = True

    created = models.DateTimeField('创建时间', default=timezone.now)
    updated = models.DateTimeField('更新时间', auto_now=True)
