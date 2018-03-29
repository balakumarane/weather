from django import template

from dateutil import parser
from datetime import datetime
from dateutil import tz
from django.utils.timezone import localtime


register = template.Library()

@register.simple_tag
def get_datetime_obj(date_time_str):
    return parser.parse(date_time_str)

@register.simple_tag
def get_formatted_datetime(date_time_str):
    tzinfos = {"UTC": +0000}
    date_obj = parser.parse(date_time_str, tzinfos=tzinfos)
    # to_zone = tz.tzlocal()
    # formatted_obj = date_obj.astimezone(to_zone)
    formatted_obj = localtime(date_obj)
    return formatted_obj.strftime("%B %d, %Y - %I:%M:%S %p")