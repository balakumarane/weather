from django.conf.urls import url
from weather_app.views import HomePage, UpdateWeather



urlpatterns = [
    url(r'^$', HomePage.as_view(template_name="weather_app/home.html"), name="home"),
    url(r'^update/$', UpdateWeather.as_view(), name='update_weather'),
]