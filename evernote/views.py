# Create your views here.
import sys

from django.shortcuts import render_to_response
from django.template import RequestContext
from django.forms.models import model_to_dict
from django.http import HttpResponse
from itertools import chain
import operator

from django.contrib.auth.models import User

import eportfoliodemo.evernote.src

def connect(request, user_id):
   	requested_user = User.objects.get(pk=user_id)
   	if (request.user.is_authenticated()):
		current_user = User.objects.get(pk=request.user.id)



	return HttpResponse('')