from django.shortcuts import render_to_response
from django.template import RequestContext
from django.contrib.auth.models import User
from eportfoliodemo.profiles.models import UserProfile

from present.models import Project

def index(request):
	
	if request.user.is_authenticated():
		projects = Project.objects.filter(owner=request.user)
        user_profile = UserProfile.objects.filter(user=request.user)
        
	return render_to_response('index.html', { 'projects':projects }, context_instance=RequestContext(request))