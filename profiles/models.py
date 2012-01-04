from django.db import models
from django.forms import ModelForm

from django.contrib.auth.models import User


class UserProfile(models.Model):
    title = models.CharField(max_length=20, blank=True)
    address = models.TextField(blank=True)
    work_phone = models.CharField(max_length=20, blank=True)
    cell_phone = models.CharField(max_length=20, blank=True)
    alternate_email_1 = models.EmailField(blank=True)
    bio = models.TextField(blank=True)
    web = models.URLField(blank=True, verify_exists=False)
    user = models.ForeignKey(User, unique=True)
    
    def __unicode__(self):
        return self.user.username + "'s Profile"
        

class UserForm(ModelForm):
    class Meta:
        model = User
        exclude = ('password','is_staff','is_active','is_superuser','last_login','date_joined','groups','user_permissions')
        
class UserProfileForm(ModelForm):
    class Meta:
        model = UserProfile
        exclude = ('user','work_phone','cell_phone','alternate_email')