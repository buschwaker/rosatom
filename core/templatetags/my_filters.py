from datetime import datetime as dt

from django import template
from django.core.cache import cache


register = template.Library()


@register.filter(name='to_age')
def to_age(value):
    date_now = dt.now().date()
    age = int((date_now - value).days / 365.25)
    return age


@register.filter
def addclass(field, css):
    return field.as_widget(attrs={'class': css})
