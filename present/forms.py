from django import forms
from eportfoliodemo.present.models import Project, ProjectType, Page, Template, TemplateType


class ProjectForm(forms.ModelForm):
    name = forms.CharField
    slug = forms.CharField
    description = forms.CharField ( widget=forms.widgets.Textarea( attrs={ 'class':'wysiwyg' } ) )
    template = forms.ModelChoiceField ( queryset=Template.objects.filter(type=TemplateType.objects.filter(name="Project Template")), empty_label=None )
    type = forms.ModelChoiceField ( queryset=ProjectType.objects.all(), empty_label=None )

    class Meta:
        model = Project



class PageForm(forms.ModelForm):
    template = forms.ModelChoiceField ( queryset=Template.objects.filter(type=TemplateType.objects.filter(name="Page Template")), empty_label=None )
    content = forms.CharField ( widget=forms.widgets.Textarea( attrs={ 'class':'wysiwyg' } ) )
    
    class Meta:
	    model = Page