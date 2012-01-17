from django.db import models
from django.forms import ModelForm

from django.contrib.auth.models import User

AVATAR_OPTIONS = (
    ('A','Georgetown Commons Avatar'),
    ('B','Gravatar'),
)

class UserProfile(models.Model):
    title = models.CharField(max_length=20, blank=True)
    address = models.TextField(blank=True)
    work_phone = models.CharField(max_length=20, blank=True)
    cell_phone = models.CharField(max_length=20, blank=True)
    alternate_email_1 = models.EmailField(blank=True)
    bio = models.TextField(blank=True)
    web = models.URLField(blank=True, verify_exists=False)
    user = models.ForeignKey(User, unique=True)
    avatar = models.CharField(max_length=1, choices=AVATAR_OPTIONS)
    avatar_email = models.CharField(max_length=200, blank=True, null=True)
    
    def __unicode__(self):
        return self.user.username + "'s Profile"
    
    def is_georgetown_user(self):
        if self.user.password == 'This is an LDAP account':
            return True
        else:
            return False
        