from django import forms
from django.forms.models import ModelForm
from eportfoliodemo.reflections.models import Reflection

class ReflectionForm(forms.ModelForm):
    class Meta:
        model = Reflection