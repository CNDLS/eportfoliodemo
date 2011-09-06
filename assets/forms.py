from django import forms
from django.forms.models import ModelForm
from eportfoliodemo.assets.models import *

class FileUploadForm(forms.Form):
    file = forms.CharField(widget=forms.widgets.FileInput(), required=True)
    