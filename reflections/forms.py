from django import forms
from django.forms.models import ModelForm
from eportfoliodemo.reflections.models import Reflection

class ReflectionForm(forms.ModelForm):
    comment = forms.CharField ( widget=forms.widgets.Textarea() )
    title = forms.CharField(label="Title (optional)")
    author = forms.CharField ( widget=forms.widgets.HiddenInput() )
    content_type = forms.CharField ( widget=forms.widgets.HiddenInput() )
    object_id = forms.CharField ( widget=forms.widgets.HiddenInput() )
    
    class Meta:
        model = Reflection