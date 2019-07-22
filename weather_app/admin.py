# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin

# Register your models here.
from weather_app.models import WeatherInfo
admin.site.register(WeatherInfo)