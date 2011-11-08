from django.http import HttpResponseRedirect, HttpResponse, HttpResponseForbidden, Http404
from django.shortcuts import render_to_response, get_object_or_404, redirect
from django.template import RequestContext

from eportfoliodemo.present.models import Project, Template
from eportfoliodemo.present.forms import ProjectForm
from datetime import datetime

# Shows a list of the user's projects
def show(request, user_id):
	projects = Project.objects.filter(owner=user_id)
	return render_to_response('present/show.html',
                    { 'projects': projects,
                    },
                    context_instance=RequestContext(request))

def display_project(request, user_id, project_slug):
	project = Project.objects.get(slug = project_slug)

	project_stylesheet = project.template.template_url + '/style.css'
	return render_to_response('present/display_project.html',
                    { 'project': project,
                      'project_stylesheet': project_stylesheet
                    },
                    context_instance=RequestContext(request))
                  
def create_project(request, user_id):
	form = ProjectForm()
	project = Project()
	if request.method == 'POST':
		for field_name in ['name','slug','description','privacy']:
			if (field_name != 'id') and (field_name[0] != "_"):
				setattr(project, field_name, request.POST[field_name])
		project.created = datetime.now()
		project.modified = datetime.now()
		template = Template.objects.get(id=request.POST['template'])
		project.template = template
		project.owner = request.user
		project.save()
		project_stylesheet = project.template.template_url + '/style.css'
		return HttpResponseRedirect(request.META['SCRIPT_NAME']+'/present/'+str(request.user.id)+'/public/'+project.slug+'/')
		# return render_to_response('present/display_project.html',
  #                   { 'project': project,
  #                     'project_stylesheet': project_stylesheet
  #                   },
  #                   context_instance=RequestContext(request))
	return render_to_response('present/create_project.html',
	 							{'form': form},
	 							context_instance=RequestContext(request)) 
