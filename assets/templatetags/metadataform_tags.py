from django import template
from eportfoliodemo.assets.forms import MetaDataForm, TagForm

register = template.Library()

@register.inclusion_tag('assets/metadata-form.html')
def display_metadata_form(request):
    metadata_form = MetaDataForm()
    return {'metadata_form':metadata_form, 'request': request}

@register.inclusion_tag('assets/tag-form.html')
def display_tag_form(request):
    tag_form = TagForm()
    return {'tag_form':tag_form, 'request': request}