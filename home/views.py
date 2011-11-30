from django.shortcuts import render_to_response
from django.template import RequestContext
from django.contrib.auth.models import User

from present.models import Project

def index(request):
	
	if request.user.is_authenticated():
		projects = Project.objects.filter(owner=request.user)
	return render_to_response('index.html', { 'projects':projects }, context_instance=RequestContext(request))