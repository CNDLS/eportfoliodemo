from django import template
register = template.Library()

'''
Import Dropbox library and the respective settings
'''
# Dropbox SDK
from dropbox.session import DropboxSession
from dropbox.client import DropboxClient
from dropbox import client, rest, session
# Dropbox app settings
from settings import DROPBOX_APP_KEY, DROPBOX_APP_SECRET, ACCESS_TYPE
from eportfoliodemo.dropboxapi.models import Dropbox



@register.simple_tag(takes_context=True)
def dropbox_folder(context, current_user, request_token, dropbox_user_id):

	sess = session.DropboxSession(DROPBOX_APP_KEY, DROPBOX_APP_SECRET, ACCESS_TYPE)
	request_token = sess.obtain_request_token()
	d = Dropbox.objects.get(user=current_user.id)
	# request_token = type(d.request_token)
	try:
		token = sess.obtain_access_token(request_token.key)
		return "Token key: %s\nToken secret: %s" % (token.key, token.secret)
	except rest.ErrorResponse, e:
		return 'Error: %s\n' % str(e)
	return ''