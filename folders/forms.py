from django.forms import ModelForm, ModelChoiceField, HiddenInput
from eportfoliodemo.folders.models import Folder

class FolderForm(ModelForm):
    owner = ModelChoiceField(label="",
                                      queryset=Folder.objects.all(),
                                      widget=HiddenInput())
    
    class Meta:
        model = Folder
        exclude = ('assets',)