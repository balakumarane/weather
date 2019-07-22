# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.contrib.postgres.fields import JSONField

# Create your models here.

class WeatherInfo(models.Model):
    place = models.CharField(max_length=62,unique=True)
    last_updated = models.DateTimeField(auto_now=True)
    image = models.ImageField(upload_to='photos',null=True, blank=True)
    data = JSONField(null=True, blank=True)

    def __unicode__(self):  # __unicode__ on Python 2
        return self.place
