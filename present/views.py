from django.http import HttpResponseRedirect, HttpResponse, HttpResponseForbidden, Http404
from django.shortcuts import render_to_response, get_object_or_404, redirect
from django.template import RequestContext

from eportfoliodemo.present.models import Project, Template, Page
from eportfoliodemo.present.forms import ProjectForm, PageForm
from datetime import datetime
from django.contrib.auth.models import User
from eportfoliodemo.libraryitems.views import get_librarytree_items_for
from eportfoliodemo.collectionitems.views import get_collectiontree_items_for

# Shows a list of the user's projects
def show(request, user_id):
	projects = Project.objects.filter(owner=user_id)
	requested_user = User.objects.get(pk=user_id)
	# get all the folders & assets.
	items_in_library_tree = get_librarytree_items_for(requested_user)
        
	# get all the collections & asset aliases.
	# it's a tree, but without hierarchy (gets us dragging, renaming, etc. parallel to lib).
	items_in_collections_tree = get_collectiontree_items_for(requested_user)
	form = ProjectForm()
	return render_to_response('present/show.html',
                    { 'projects': projects,
                      'folder_nodes': items_in_library_tree,
                      'collections_nodes': items_in_collections_tree,
                      'form': form
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
		return HttpResponse('blah', mimetype='text/plain')

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
		# Attach the page to the respective project
		project.pages.add(page)
		return HttpResponseRedirect(request.META['SCRIPT_NAME']+'/present/'+str(request.user.id)+'/public/'+project.slug+'/')

	return render_to_response('present/create_page.html',
	 							{'form': form},
	 							context_instance=RequestContext(request))
