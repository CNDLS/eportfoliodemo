from django import forms
from django.forms.models import ModelForm
from eportfoliodemo.assets.models import CustomMetaData
import tagging
from tagging.models import Tag
from tagging.fields import TagField

class FileUploadForm(forms.Form):
    file = forms.CharField(widget=forms.widgets.FileInput(), required=True)

class MetaDataForm(forms.ModelForm):
    class Meta:
        model = CustomMetaData

class TagForm(forms.ModelForm):
    class Meta:
        model = Tag
    