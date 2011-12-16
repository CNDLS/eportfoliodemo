from django import template
from django.template.defaultfilters import stringfilter

register = template.Library()

@register.filter(name='is_composition')

@stringfilter
def is_composition(path):
    return path.find('compose') > 0