# Create your views here.
from django.shortcuts import render_to_response
from django.template import RequestContext
from django.forms.models import model_to_dict

from django.contrib.auth.models import User
from profiles.models import UserProfile, UserProfileForm


import logging
logger = logging.getLogger(__name__)



def index(request):
    try:
        user_profile = UserProfile.objects.get_or_create(user=User.objects.get(request.user.id))
    except:
        user_profile = UserProfile(user=request.user)
        user_profile.save()
        
    finally:
        user_profile = model_to_dict(user_profile)
        return render_to_response('profiles/index.html', { 'user_profile': user_profile }, context_instance=RequestContext(request))
    
    
    
def edit(request):
    try:
        user_profile = UserProfile.objects.get(user=request.user.id)
    except:
        user_profile = UserProfile()
        user_profile.save()
    finally:
        user_profile_form = UserProfileForm(instance=user_profile)
        user_profile = user_profile_form.save(commit=False)
        user_profile.title = 'Mr'
        user_profile.save()
        
        return render_to_response('profiles/edit.html', { 'user_profile': user_profile, 'user_profile_form': user_profile_form }, context_instance=RequestContext(request))