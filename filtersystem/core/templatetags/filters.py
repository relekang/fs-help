import re

from django.template.base import Library

register = Library()


@register.filter
def comma_list(list):
    return ', '.join([str(item) for item in list])


@register.filter
def boolean(value):
    return value


@register.filter
def excerpt(value):
    for s in re.findall('<img src=".*"[ ]+\/>', value):
        value = value.replace(s, '')
    for s in re.findall('<p>', value):
        value = value.replace(s, '')
    for s in re.findall('<\/p>', value):
        value = value.replace(s, '')
    return value[:400].strip()
