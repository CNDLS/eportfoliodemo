# Create your views here.
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
    # make user_profile from post
    user_profile = UserProfile.objects.get(user=user_id)
    for field_name in user_profile._meta.get_all_field_names():
        # don't need primary key, user, or many-to-many associations
        if (field_name != 'id') and (field_name != 'user') and (field_name[0] != "_"):
            setattr(user_profile, field_name, request.POST[field_name])
    user_profile_form = UserProfileForm(instance=user_profile)
    
    # hoy, pronto! make user from post, too.
    user = User.objects.get(pk=user_id)
    for field_name in ['username','first_name','last_name','email']:
        setattr(user, field_name, request.POST[field_name])
    user_form = UserForm(instance=user)
    
    # if user_profile_form.is_valid() and user_form.is_valid():
    user_profile.save()
    user.save()
        
    return redirect('profiles/' + str(user_profile.user_id))
    