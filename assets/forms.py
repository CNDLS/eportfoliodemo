from django import forms
from django.forms.models import ModelForm
from eportfoliodemo.assets.models import CustomMetaData

class FileUploadForm(forms.Form):
    file = forms.CharField(widget=forms.widgets.FileInput(), required=True)

class MetaDataForm(forms.ModelForm):
    class Meta:
        model = CustomMetaData
    