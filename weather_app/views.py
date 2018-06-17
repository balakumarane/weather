# -*- coding: utf-8 -*-
from __future__ import unicode_literals

import urllib, json
from datetime import timedelta

from django.shortcuts import render, get_object_or_404
from django.views.generic import TemplateView, RedirectView
from django.conf import settings
from django.utils import timezone
from django.urls import reverse

from weather_app.models import WeatherInfo
# Create your views here.
def update_to_db():
    url = settings.FACEBOOK_URL
    response = urllib.urlopen(url)
    if response.code == 200:
        data = json.loads(response.read())
        weather_obj, obj_status = WeatherInfo.objects.get_or_create(place='chennai')
        weather_obj.data = data
        weather_obj.save()
        return weather_obj
    else:
        return False


class HomePage(TemplateView):
    def get_context_data(self, **kwargs):
        context = super(HomePage, self).get_context_data(**kwargs)
        try:
            weather_obj = WeatherInfo.objects.get(place='chennai')
        except:
            print "except"
            weather_obj = update_to_db()
        time_threshold = weather_obj.last_updated + timedelta(hours=1)
        if timezone.now() > time_threshold:
            ## update the db
            print "Updating ..."
            weather_obj = update_to_db()
        context.update({'data': weather_obj.data,'weather_obj': weather_obj, 'current_time': timezone.now()})
        return context

class UpdateWeather(RedirectView):
    # url = reverse('home')
    # url ='/'

    def get_redirect_url(self, *args, **kwargs):
        update_to_db()
        return reverse('home')