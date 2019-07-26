# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.contrib.postgres.fields import JSONField
from django.conf import settings

if settings.DEBUG:
    from django.core.files.storage import FileSystemStorage as Storage
else:
    from minio_storage.storage import MinioMediaStorage as Storage

class OverwriteStorage(Storage):   
    def get_available_name(self, name, max_length=None):
        """
        Returns a filename that's free on the target storage system, and
        available for new content to be written to.
        """
        # If the filename already exists, remove it as if it was a true file system
        if self.exists(name):
            self.delete(name)
        return name

        
class WeatherInfo(models.Model):
    place = models.CharField(max_length=62,unique=True)
    last_updated = models.DateTimeField(auto_now=True)
    image = models.ImageField(upload_to='photos',storage=OverwriteStorage(), null=True, blank=True)
    data = JSONField(null=True, blank=True)

    def __unicode__(self):  # __unicode__ on Python 2
        return self.place
