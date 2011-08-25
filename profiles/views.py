# Create your views here.
from django.shortcuts import render_to_response
from django.template import RequestContext
from django.forms.models import model_to_dict

from django.contrib.auth.models import User
from profiles.models import UserForm, UserProfile, UserProfileForm


import logging
logger = logging.getLogger(__name__)


# index = list user profiles available to current user.
# for students, this should redirect to display of their own.
def index(request):
    user_profiles = UserProfile.objects.all()
    return render_to_response('profiles/index.html', { 'user_profiles': user_profiles }, context_instance=RequestContext(request))



# show user profile for a designated user (cf. permissions)
def show(request, user_id):
    requested_user = User.objects.get(pk=user_id)
    logger.debug(requested_user)
    try:
        user_profile, ok = UserProfile.objects.get_or_create(user=requested_user)
    except:
        user_profile = UserProfile(user=requested_user)
        user_profile.save()
        
    finally:
        if (ok):
            user = model_to_dict(user_profile.user)
        else:
            user = model_to_dict(requested_user)
        user_profile = model_to_dict(user_profile)
        return render_to_response('profiles/show.html', { 'user_profile': user_profile, 'user':user }, context_instance=RequestContext(request))
    
    
    
def edit(request, user_id):
    requested_user = User.objects.get(pk=user_id)
    try:
        user_profile, ok = UserProfile.objects.get_or_create(user=requested_user)
    except:
        user_profile = UserProfile(user=requested_user)
        user_profile.save()
    finally:
        user_form = UserForm(instance=requested_user)
        user_profile_form = UserProfileForm(instance=user_profile)
        user_profile = user_profile_form.save()
        
        return render_to_response('profiles/edit.html', { 'user_profile_form': user_profile_form, 'user_form': user_form }, context_instance=RequestContext(request))