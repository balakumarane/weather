from django.conf.urls import url
from weather_app.views import HomePage, UpdateWeather, WeatherPage



urlpatterns = [
    # url(r'^$', HomePage.as_view(template_name="weather_app/homepage.html"), name="home"),
    url(r'^weather/$', WeatherPage.as_view(template_name="weather_app/weather.html"), name="weather_page"),
    url(r'^$', WeatherPage.as_view(template_name="weather_app/weather.html"), name="weather_page"),
    url(r'^update/$', UpdateWeather.as_view(), name='update_weather'),
]