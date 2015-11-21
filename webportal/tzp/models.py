# -*- coding: utf-8 -*-

from django.db import models

# Create your models here.


class TimeZoneModel(models):
    title = models.CharField(max_length=20, unique=True)
    shift = models.SmallIntegerField(default=None)
    image = models.ImageField()
