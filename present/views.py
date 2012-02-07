import sys

from django.http import HttpResponseRedirect, HttpResponse, HttpResponseForbidden, Http404
from django.shortcuts import render_to_response, get_object_or_404, redirect
from django.template import RequestContext

from eportfoliodemo.present.models import Project, ProjectType, Template, Page, PageItem
from eportfoliodemo.present.forms import ProjectForm, PageForm
from datetime import datetime
from django.contrib.auth.models import User
from eportfoliodemo.libraryitems.views import get_librarytree_items_for
from eportfoliodemo.collectionitems.views import get_collectiontree_items_for

from eportfoliodemo.reflections.models import Reflection
from eportfoliodemo.reflections.views import get_content_type_and_object

from django.contrib.contenttypes.models import ContentType

from eportfoliodemo.assets.models import Asset, AssetAlias
from eportfoliodemo.settings import MEDIA_ROOT, AJAX_PREFIX
from eportfoliodemo.settings import PRIVACY, PROJECT_TEMPLATE_LOCATION, PROJECT_TEMPLATE_URL

from django.core import serializers
from django.utils import simplejson



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

	project_stylesheet = PROJECT_TEMPLATE_URL + project.template.template_path + 'style.css'
	project_template_name = 'basic' # temp.
	
	return render_to_response('present/display_project.html',
								{ 'project': project,
								  'project_template_name': project_template_name,
								  'project_stylesheet': project_stylesheet,
								  'AJAX_PREFIX': AJAX_PREFIX
								},
								context_instance=RequestContext(request))
				  
				  
				  
def create_project(request, user_id, project_slug = None):
	form = ProjectForm()
	

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
		# current_form = {}
		# current_form = {'name': project.name, 'slug': project.slug, 'description':project.description, 'privacy':project.privacy, 'template':project.template.name}
		# json_serializer = serializers.get_serializer("json")()
		# current_form = json_serializer.serialize([current_form])
		# return HttpResponse(form, mimetype='text/plain')
		# return HttpResponse(simplejson.dumps(current_form))
		
		
		return render_to_response('present/editform.html', { 'form': form, 'project_slug':project_slug }, context_instance=RequestContext(request))

	if request.method == 'POST':
		# try:
		# 	project = Project.objects.get(owner=user_id, slug=project_slug)
		# except:
		# 	project = Project()
		try:
			project = Project.objects.get(owner=user_id, slug=request.POST['project_slug'])
		except:
			project = Project()
		for field_name in ['name','slug','description','privacy']:
			if (field_name != 'id') and (field_name[0] != "_"):
				setattr(project, field_name, request.POST[field_name])
		project.created = datetime.now()
		project.modified = datetime.now()
		proejct_type = ProjectType.objects.get(id=request.POST['type'])
		project.type = proejct_type
		template = Template.objects.get(id=request.POST['template'])
		project.template = template
		project.owner = request.user
		project.save()

		# Create a default page for the project

		# Assigning the basic page template
		page_template = Template.objects.get(id=2)
		
		page = Page()
		page.name = 'Home'
		page.slug = 'home'
		page.owner = request.user
		page.created = datetime.now()
		page.modified = datetime.now()
		# Default permission is protected - that is public but not indexed by search engines
		page.privacy = 1
		page.template = page_template

		page.save()
		project.pages.add(page)
		project.save()

		return HttpResponseRedirect(request.META['SCRIPT_NAME']+'/present/'+str(request.user.id)+'/public/'+project.slug+'/')

	# return render_to_response('present/create_project.html',
	#  							{'form': form},
	#  							context_instance=RequestContext(request))
	return render_to_response('present/editform.html', { 'form': form, 'project_slug':project_slug }, context_instance=RequestContext(request))
	 							

	 							
def compose_project(request, user_id, project_slug=None):
	project = Project.objects.get(slug=project_slug)
	requested_user = User.objects.get(pk=user_id)
	if (request.user.is_authenticated()):
		current_user = User.objects.get(pk=request.user.id)

	project_template_name = 'basic' # temp.
	
	# get all the folders & assets.
	items_in_library_tree = get_librarytree_items_for(requested_user)
	
	# get all the collections & asset aliases.
	# it's a tree, but without hierarchy (gets us dragging, renaming, etc. parallel to lib).
	items_in_collections_tree = get_collectiontree_items_for(requested_user)

	project_stylesheet = PROJECT_TEMPLATE_URL + project.template.template_path + 'style.css'
	# return render_to_response('present/editform.html', { 'form': form, 'project_slug':project_slug }, context_instance=RequestContext(request))
	projects = Project.objects.filter(owner=request.user)

	return render_to_response('present/compose_project.html', { 'project': project,
																'project_stylesheet': project_stylesheet,
																'project_template_name': project_template_name,
																'requested_user': requested_user,
																'current_user': current_user,
																'folder_nodes': items_in_library_tree,
																'collections_nodes': items_in_collections_tree,
																'AJAX_PREFIX': AJAX_PREFIX,
																'projects': projects },
																  context_instance=RequestContext(request))
	# return render_to_response('present/create_project.html',
	#  							{'form': form},
	#  							context_instance=RequestContext(request))



def project_in_template(request, user_id, project_slug=None):
	project = Project.objects.get(slug=project_slug)
	requested_user = User.objects.get(pk=user_id)
	project_stylesheet = PROJECT_TEMPLATE_URL + project.template.template_path + 'style.css'
	
	return render_to_response('present/compose_project.html', { 'project': project,
																'project_stylesheet': project_stylesheet, 
																'requested_user': requested_user,
																  'AJAX_PREFIX': AJAX_PREFIX },
																  context_instance=RequestContext(request))



def add_page(request, user_id, project_slug=None):
	project = Project.objects.get(owner=user_id, slug=project_slug)
	form = PageForm()
	page = Page()

	if request.method == 'POST':
		for field_name in ['name','slug','privacy','content']:
			if (field_name != 'id') and (field_name[0] != "_"):
				setattr(page, field_name, request.POST[field_name])
		page.created = datetime.now()
		page.modified = datetime.now()
		page.owner = request.user
		template = request.POST['template']
		template_obj = Template.objects.get(id=template)
		page.template = template_obj
		page.save()
		# Attach the page to the respective project
		project.pages.add(page)
		return HttpResponseRedirect(request.META['SCRIPT_NAME']+'/present/'+str(request.user.id)+'/'+project.slug+'/compose/')

	return render_to_response('present/create_page.html',
	 							{'form': form, 'project': project}, context_instance=RequestContext(request))

def edit_page_content(request, user_id, page_id=None, project_id=None):
	page = Page.objects.get(pk=page_id)
	project = Project.objects.get(pk=project_id)
	
	if request.method == 'POST':
		page.content = request.POST["content"]
		page.save()
		
		json_serializer = serializers.get_serializer("json")()
		page_array = [json_serializer.serialize([page])] 
		return HttpResponse (page_array, mimetype='application/json')
	else:
		form = PageForm(instance=page)
		return render_to_response('present/edit_page_content.html', { 'form': form, 'action': 'edit', 'project': project, 'page': page }, context_instance=RequestContext(request))
	

def get_page_content(request, user_id, page_id=None, project_id=None):
	project = Project.objects.get(id=project_id)
	pages = project.pages.all()

	request_page = Page.objects.get(id=page_id)
	json_serializer = serializers.get_serializer("json")() 
	
	if request_page in pages:
		asset = False
		page_array = [json_serializer.serialize([request_page])] 
		page_items = PageItem.objects.filter(page=page_id)

		for page_item in page_items:
			content_type = ContentType.objects.get(pk=page_item.content_type_id)
			
			if content_type.model_class() == AssetAlias:
				asset = Asset.objects.get(pk=page_item.object_id)
				page_item_content_object = asset
			else:
				page_item_content_object = content_type.get_object_for_this_type(pk=page_item.object_id)
				
			
			# special processing. doesn't seem to work as a method on the model object
		 	if (content_type.model_class() == Reflection):
		 		source_object = page_item_content_object.content_object
		 		if (type(source_object) == AssetAlias):
		 			source_object = Asset.objects.get(pk=source_object.asset_id)
		 		page_item_content_object.source_object = json_serializer.serialize([source_object])
				page_item_content_object.title = "on '" + source_object.name + "'"
			elif content_type.model_class() == Asset:
				page_item_content_object.html_content = page_item_content_object.contents()
				# print "page_item_content_object.html_content " + page_item_content_object.html_content
			
			page_item_dict = {}
			page_item_dict["page_item"] = json_serializer.serialize([page_item])
			page_item_dict["content_object"] = json_serializer.serialize([page_item_content_object])

			page_array.append( page_item_dict )
		
		page_data = simplejson.dumps( page_array )

	return HttpResponse (page_data, mimetype='application/json')
	
	
def add_content(request, user_id, content_type, object_id, project_slug, page_id):
	project = Project.objects.get(owner=user_id, slug=project_slug)
	request_page = Page.objects.get(id=page_id)
	obj_array = get_content_type_and_object(content_type, object_id)

	obj = obj_array[1]
	json_serializer = serializers.get_serializer("json")()

	if content_type == 'assetalias':
		asset = obj.asset
	else:
		asset = obj
		
	asset.html_content = asset.contents()	
	# print "asset.html_content " + asset.html_content
	# asset.save()
		
	page_item = PageItem()
	page_item.content_object = asset
	page_item.page = request_page

	# store the path spec into the node of the doc where the content was added.
	if request.method == 'POST':
		page_item.page_section_tag_selector = request.POST['page_section_tag_selector']  # '#basic-page_content'
		
	page_item.ordinal = 0
	page_item.save()

	obj_data = [asset]
	json_obj = json_serializer.serialize(obj_data)
	return HttpResponse(json_obj, mimetype='application/json')
