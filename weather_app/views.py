# -*- coding: utf-8 -*-
from __future__ import unicode_literals

import json
import urllib.request as urllib
from urllib import request
import os
from datetime import timedelta
from django.core.files import File

from django.shortcuts import render, get_object_or_404
from django.views.generic import TemplateView, RedirectView, View
from django.conf import settings
from django.utils import timezone
from django.urls import reverse
from django.http import JsonResponse
from fcm_django.models import FCMDevice

from weather_app.models import WeatherInfo
# Create your views here.
def update_to_db():
    url = settings.FACEBOOK_URL
    url2 = settings.FACEBOOK_URL2
    image = False
    fb = False
    weather_obj, obj_status = WeatherInfo.objects.get_or_create(place='chennai')
    try:
        result = request.urlretrieve(settings.WEATHER_IMAGE_URL)
        weather_obj.image.save(
                    os.path.basename(settings.WEATHER_IMAGE_URL),
                    File(open(result[0], 'rb'))
                    )
        weather_obj.save()
        image = True
        print("Image Update -- SUCCESS !!!")
    except:
        print("Image Update -- FAILED FAILED !!!")
        pass

    try:
        response = urllib.urlopen(url)
        response2 = urllib.urlopen(url2)
        if response.code == 200 or response2.code == 200:
            data = []
            # import pdb; pdb.set_trace()
            if response.code == 200:
                data1  = (json.loads(response.read()))
                data.extend(data1['data'])
            if response2.code == 200:
                data2  = (json.loads(response2.read()))
                data.extend(data2['data'])
            if data != weather_obj.data:
                # FCM -- Send Push Notification
                devices = FCMDevice.objects.all()
                message = data[0]['message'][:100]
                devices.send_message(title="Weather Update !!!", body=message, click_action= 'https://weather.zapto.org/', icon='https://bk.sytes.net/weather-static/images/bk_192.png')
                        
            weather_obj.data = data
            weather_obj.save()
            print("FB Update -- SUCCESS !!!")
            fb = True
        else:
            print("FB Update -- FAILED FAILED !!!")
            return False            
    except:
        print("Updating Failed!!!")

    return weather_obj,{'FB': fb, 'IMAGE': image}


class HomePage(TemplateView):
    def get_context_data(self, **kwargs):
        context = super(HomePage, self).get_context_data(**kwargs)
        try:
            weather_obj = WeatherInfo.objects.get(place='chennai')
        except:
            print("except")
            weather_obj,status = update_to_db()
        time_threshold = weather_obj.last_updated + timedelta(hours=1)
        if timezone.now() > time_threshold:
            ## update the db
            print("Updating ...")
            weather_obj,status = update_to_db()
        context.update({'data': weather_obj.data,'weather_obj': weather_obj, 'current_time': timezone.now()})
        return context

class WeatherPage(TemplateView):
    def get_context_data(self, **kwargs):
        context = super(WeatherPage, self).get_context_data(**kwargs)
        try:
            weather_obj = WeatherInfo.objects.get(place='chennai')
        except:
            print("except")
            weather_obj,status = update_to_db()
        time_threshold = weather_obj.last_updated + timedelta(hours=1)
        if timezone.now() > time_threshold:
            ## update the db
            print("Updating ...")
            weather_obj,status = update_to_db()
        context.update({'data': weather_obj.data,'weather_obj': weather_obj, 'current_time': timezone.now()})
        return context        

class UpdateWeather(RedirectView):
    # url = reverse('home')
    # url ='/'

    def get_redirect_url(self, *args, **kwargs):
        update_to_db()
        return reverse('weather_home_page')

class UpdateWeatherApp(View):

    def get(self, request, *args, **kwargs):
        weather_obj,status = update_to_db()
        return JsonResponse(status)
