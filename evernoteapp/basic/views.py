from datetime import datetime
from django.core.urlresolvers import reverse
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render_to_response
from django.template import RequestContext
from eportfoliodemo.evernoteapp.evernote_auth import EvernoteAPI
import logging

def landing(request):
    return render_to_response('evernoteapp/home.html', {},
            context_instance=RequestContext(request))

def run_evernote_auth(request):
    """ Starts the OAuth token obtaining process by obtaining the token we use
        to request the user's token
    """
    callback_url = request.build_absolute_uri(reverse(
        'eportfoliodemo.evernoteapp.basic.views.get_evernote_token', args=[]))
            
    everAuth = EvernoteAPI()
    tok = everAuth.get_token(request, callback_url)
    return tok

def get_evernote_token(request):
    """ View that handles the callback from the Evernote OAuth call and
        stores the OAuth token for the user
    """
    if request.user.is_authenticated:
        everAuth = EvernoteAPI()
        credentials = everAuth.get_user_token(request)
        # credentials here contain OAuth token, save it!
        profile = request.user.profile
        logging.error(credentials['expires'])
        try:
            expires_time = datetime.fromtimestamp(int(credentials['expires']))
        except TypeError:
            logging.error("Error parsing token expires time")
            expires_time = datetime.now()
        profile.evernote_token = credentials['oauth_token']
        profile.evernote_token_expires_time = expires_time
        profile.save()
    return HttpResponseRedirect(reverse('eportfoliodemo.evernoteapp.basic.views.post_evernote_token',
        args=[]))
 
def post_evernote_token(request):
    return render_to_response('evernote_resp.html', {},
            context_instance=RequestContext(request))
