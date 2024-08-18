from django import template
from datetime import datetime, timedelta, timezone
from django.utils.timesince import timesince
from django.utils.timezone import localtime

register = template.Library()

@register.simple_tag
def get_cookie(request, cookie_name):
    return request.COOKIES.get(cookie_name, '')

@register.simple_tag
def rmv_midnight(datetime_obj):
    date_string = datetime_obj.strftime("%b. %d, %Y, %I:%M %p")
    date_string_parts = date_string.split(", ")
    date_string_without_time = ", ".join(date_string_parts[:-1])
    return date_string_without_time


@register.filter(name='format_timesince')
def format_timesince(value):
    """
    Custom template filter to convert a datetime to timesince format.
    """
    # Ensure the datetime is in the current timezone
    value = localtime(value)
    
    # Get the timesince value and remove the "ago" suffix
    timesince_str = timesince(value).split(' ')[0]

    # Map the timesince components to user-friendly labels
    mapping = {
        'year': 'y',
        'years': 'y',
        'month': 'mo',
        'months': 'mo',
        'week': 'w',
        'weeks': 'w',
        'day': 'd',
        'days': 'd',
        'hour': 'h',
        'hours': 'h',
        'minute': 'm',
        'minutes': 'm',
        'second': 's',
        'seconds': 's',
    }

    # Replace the timesince components with user-friendly labels
    for key, value in mapping.items():
        timesince_str = timesince_str.replace(key, value)

    return timesince_str