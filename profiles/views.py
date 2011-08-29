# Create your views here.
import sys

from django.shortcuts import render_to_response, redirect
from django.template import RequestContext
from django.forms.models import model_to_dict
from django.http import HttpResponse

from django.contrib.auth.models import User
from eportfoliodemo.profiles.models import UserForm, UserProfile, UserProfileForm


import logging
logger = logging.getLogger(__name__)


# index = list user profiles available to current user.
# for students, this should redirect to display of their own.
def index(request):
    current_user = User.objects.get(pk=request.user.id)
    current_user_profile, created = UserProfile.objects.get_or_create(user=request.user)
    if (created):
        return redirect(str(request.user.id) + '/edit')
    elif (current_user.is_superuser):
        user_profiles = UserProfile.objects.all()
        return render_to_response('profiles/index.html', { 'user_profiles': user_profiles, 'current_user': current_user }, context_instance=RequestContext(request))
    else:
        return redirect('profiles/' + str(request.user.id))


# show user profile for a designated user (cf. permissions)
def show(request, user_id):
    requested_user = User.objects.get(pk=user_id)

    try:
        user_profile, created = UserProfile.objects.get_or_create(user=requested_user)
    except:
        user_profile = UserProfile(user=requested_user)
        user_profile.save()
        
    finally:
        if (created):
            user = model_to_dict(user_profile.user)
        else:
            user = model_to_dict(requested_user)
        user_profile = model_to_dict(user_profile)
        return render_to_response('profiles/show.html', { 'user_profile': user_profile, 'user':user }, context_instance=RequestContext(request))
    
    
    
def edit(request, user_id):
    requested_user = User.objects.get(pk=user_id)
    
    try:
        user_profile, created = UserProfile.objects.get_or_create(user=requested_user)
    except:
        user_profile = UserProfile(user=requested_user)
        user_profile.save()
        
    finally:
        user_form = UserForm(instance=requested_user)
        user_profile_form = UserProfileForm(instance=user_profile)
    
        return render_to_response('profiles/edit.html', { 'user_profile_form': user_profile_form, 'user_form': user_form }, context_instance=RequestContext(request))
        


# requires request.method == "POST"
def update(request, user_id):
    # user_form = UserForm(request.POST, instance=User())
    user_profile_form = UserProfileForm(request.POST, instance=UserProfile())
    # if 
    # user_form.is_valid() 
    user_profile_form.is_valid()
    # user = user_form.save()
    user_profile = user_profile_form.save()
    return redirect('profiles/' + str(user_profile.user_id))
    