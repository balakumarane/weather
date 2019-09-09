from weather_app.views import HomePage, UpdateWeather, WeatherPage, UpdateWeatherApp
from django.conf.urls import url
from django.views.generic import TemplateView



urlpatterns = [
    # url(r'^$', HomePage.as_view(template_name="weather_app/homepage.html"), name="home"),
    url(r'^weather/$', WeatherPage.as_view(template_name="weather_app/weather.html"), name="weather_page"),
    url(r'^$', WeatherPage.as_view(template_name="weather_app/weather.html"), name="weather_home_page"),
    url(r'^privacy-policy/$', TemplateView.as_view(template_name="weather_app/privacy_policy.html"), name="weather_privacy_policy"),
    url(r'^update/$', UpdateWeather.as_view(), name='update_weather'),
    url(r'^updateweather/$', UpdateWeatherApp.as_view(), name='update_weather_app'),
]