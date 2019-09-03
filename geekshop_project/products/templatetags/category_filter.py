from django import template
import datetime

register = template.Library()
@register.filter
def about(value):
    return 'Описание категории: ' + value

@register.simple_tag
def current_time():
    return datetime.datetime.now()
