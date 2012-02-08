from django import forms
from django.forms.models import ModelForm
from eportfoliodemo.assets.models import CustomMetaData
import tagging
from tagging.models import Tag
from tagging.fields import TagField
from assets.models import Asset

class FileUploadForm(forms.Form):
	file = forms.CharField(widget=forms.widgets.FileInput(), required=True)

class MetaDataForm(forms.ModelForm):
	class Meta:
		model = CustomMetaData

class TagForm(forms.ModelForm):
	class Meta:
		model = Tag
	
class AssetForm(forms.ModelForm):
	name = forms.CharField
	description = forms.CharField ( widget=forms.widgets.Textarea( attrs={ 'class':'wysiwyg' } ) )
	owner = forms.CharField ( widget=forms.widgets.HiddenInput() )
		
	class Meta:
		model = Asset
		exclude = ('file','created','modified','size','html_content','filetype','reflection','custom_meta_data')