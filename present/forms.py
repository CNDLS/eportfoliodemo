from django import forms
from django.forms.models import ModelForm
from eportfoliodemo.present.models import Project, Page

class ProjectForm(forms.ModelForm):
    class Meta:
        model = Project

class PageForm(forms.ModelForm):
	class Meta:
		model = Page