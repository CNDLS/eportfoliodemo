from django.forms import ModelForm, ModelChoiceField, HiddenInput
from eportfoliodemo.usercollections.models import Collection

class CollectionForm(ModelForm):
    owner = ModelChoiceField(label="",
                                      queryset=Collection.objects.all(),
                                      widget=HiddenInput())
    
    class Meta:
        model = Collection
        exclude = ('parent')