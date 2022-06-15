from datetime import datetime as dt

from django import template


register = template.Library()


@register.filter(name='to_age')
def to_age(value):
    """Фильтр, приводящий дату рождения к возрасту(количество полных лет)"""
    date_now = dt.now().date()
    age = int((date_now - value).days / 365.25)
    return age


@register.filter
def addclass(field, css):
    """Фильтр, позволяющий заполнить аттрибут class"""
    return field.as_widget(attrs={'class': css})
