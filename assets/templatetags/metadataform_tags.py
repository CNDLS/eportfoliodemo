from django import template
from eportfoliodemo.assets.forms import MetaDataForm

register = template.Library()

@register.inclusion_tag('assets/metadata-form.html')
def display_metadata_form(request):
    metadata_form = MetaDataForm()
    return {'metadata_form':metadata_form, 'request': request}