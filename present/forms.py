from django import forms
from django.forms.models import ModelForm
from eportfoliodemo.present.models import Project

class ProjectForm(forms.ModelForm):
    class Meta:
        model = Project