from django.db import models
from django.forms import ModelForm

from django.contrib.auth.models import User


class UserProfile(models.Model):
    title = models.TextField(blank=True)
    address = models.TextField(blank=True)
    work_phone = models.CharField(max_length=20, blank=True)
    cell_phone = models.CharField(max_length=20, blank=True)
    alternate_email_1 = models.EmailField(blank=True)
    bio = models.TextField(blank=True)
    web = models.URLField(blank=True, verify_exists=False)
    user = models.ForeignKey(User, unique=True)
    
    def __unicode__(self):
        return self.user.username + "'s Profile"
        

class UserProfileForm(ModelForm):
    class Meta:
        model = UserProfile