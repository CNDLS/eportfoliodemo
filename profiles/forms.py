from django.forms import ModelForm

from django.contrib.auth.models import User
from eportfoliodemo.profiles.models import UserProfile

class UserForm(ModelForm):
    class Meta:
        model = User
        #TODO: Remove password from exclusion list since we can allow a user to change the password if it is a local user
        #TODO: Put the necessary views in place for changing password
        exclude = ('username','email','password','is_staff','is_active','is_superuser','last_login','date_joined','groups','user_permissions')
        
class UserProfileForm(ModelForm):
    class Meta:
        model = UserProfile
        exclude = ('user','work_phone','cell_phone','alternate_email')

