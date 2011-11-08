from django.http import HttpResponseRedirect, HttpResponse, HttpResponseForbidden, Http404
from django.shortcuts import render_to_response, get_object_or_404, redirect
from django.template import RequestContext

from eportfoliodemo.present.models import Project, Template, Page
from eportfoliodemo.present.forms import ProjectForm, PageForm
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
                  
def create_project(request, user_id, project_slug = None):
	form = ProjectForm()
	project = Project()

	# If a project needs to be updated, then supply the form with the current values
	if project_slug != None:
		project = Project.objects.get(owner=user_id, slug=project_slug)
		form = ProjectForm(initial={
			'name': project.name,
			'slug': project.slug,
			'description': project.description,
			'privacy': project.privacy,
			'template': project.template
		})

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
		#project_stylesheet = project.template.template_url + '/style.css'
		return HttpResponseRedirect(request.META['SCRIPT_NAME']+'/present/'+str(request.user.id)+'/public/'+project.slug+'/')

	return render_to_response('present/create_project.html',
	 							{'form': form},
	 							context_instance=RequestContext(request))

def add_page(request, user_id, project_slug=None):
	project = Project.objects.get(owner=user_id, slug=project_slug)
	form = PageForm()
	page = Page()

	if request.method == 'POST':
		for field_name in ['name','slug','content', 'privacy']:
			if (field_name != 'id') and (field_name[0] != "_"):
				setattr(page, field_name, request.POST[field_name])
		page.created = datetime.now()
		page.modified = datetime.now()
		page.owner = request.user
		page.save()
		project.pages.add(page)
		return HttpResponseRedirect(request.META['SCRIPT_NAME']+'/present/'+str(request.user.id)+'/public/'+project.slug+'/')

	return render_to_response('present/create_page.html',
	 							{'form': form},
	 							context_instance=RequestContext(request))
