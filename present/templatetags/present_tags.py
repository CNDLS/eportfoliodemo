from django import template
from django.template.defaultfilters import stringfilter
from django.template import loader_tags, Template
from django.conf import settings
from django.template.loader import find_template
# from django.template.loader_tags import BaseIncludeNode
# from django.template.base import TemplateSyntaxError, TemplateDoesNotExist

register = template.Library()

@register.filter(name='is_composition')

@stringfilter
def is_composition(path):
    return path.find('compose') > 0
    
@register.simple_tag
def editable_state(path):
	if is_composition(path):
		return "editable"
	else:
		return ""