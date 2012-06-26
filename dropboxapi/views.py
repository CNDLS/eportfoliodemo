from eportfoliodemo.dropboxapi.models import Dropbox
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, redirect
from django.template import RequestContext
from django.contrib.auth.models import User

'''
Import Dropbox library and the respective settings
'''
# Dropbox SDK
from dropbox.session import DropboxSession
from dropbox.client import DropboxClient
from dropbox import client, rest, session
# Dropbox app settings
from settings import DROPBOX_APP_KEY, DROPBOX_APP_SECRET, ACCESS_TYPE


def callback(request, user_id):
	sess = session.DropboxSession(DROPBOX_APP_KEY, DROPBOX_APP_SECRET, ACCESS_TYPE)
	request_token = sess.obtain_request_token()
	try:
		token = sess.obtain_access_token(request_token)
		return "Token key: %s\nToken secret: %s" % (token.key, token.secret)
	except rest.ErrorResponse, e:
		return 'Error: %s\n' % str(e)
		# return render(request, 'library/show.html',{'e':e})
	return HttpResponseRedirect('/library/1/')



# def initialize(request, user_id):
# 	TOKEN_STORE = {}

# 	sess = session.DropboxSession(DROPBOX_APP_KEY, DROPBOX_APP_SECRET, ACCESS_TYPE)

# 	request_token = sess.obtain_request_token()
# 	TOKEN_STORE[request_token.key] = request_token
# 	redirect_url = 'http://localhost:7000/library/1/'
# 	url = sess.build_authorize_url(request_token,redirect_url)
# 	user_obj = User.objects.get(id=user_id)
# 	try:
# 		d = Dropbox.objects.get(user=user_obj)
# 		d.request_token = request.GET['oauth_token']
# 		d.dropbox_user_id = request.GET['uid']
# 		d.access_token = token
# 		d.save()
# 	except Dropbox.DoesNotExist:
# 		d = Dropbox()
# 		# d.request_token = request.GET['oauth_token']
# 		# d.dropbox_user_id = request.GET['uid']
# 		# d.access_token = token
# 		d.user = user_obj
# 		d.save()
# 	return render(request, 'dropboxapi/initialize.html',{'url':url})



'''
OLD STUFF - VERSION 2
'''
def initialize(request, user_id):
	# handle = DropboxHandler()
	# url = handle.get_url()
	blah = []
	TOKEN_STORE = {}
	sess = session.DropboxSession(DROPBOX_APP_KEY, DROPBOX_APP_SECRET, ACCESS_TYPE)
	request_token = sess.obtain_request_token()

	# TOKEN_STORE[request_token.key] = request_token
	blah.append(request_token)
	# redirect_url = 'http://localhost:7000/library/1/'
	redirect_url = 'http://localhost:7000/dropbox/1/callback/'
	# redirect_url = 'http://localhost:7000/dropbox/1/initialize/'
	url = sess.build_authorize_url(request_token,redirect_url)
	user_obj = User.objects.get(id=user_id)
	# try:
	# 	token = sess.obtain_access_token(request_token)
	# 	return 'sd'
	# 	# return "Token key: %s\nToken secret: %s" % (token.key, token.secret)
	# except rest.ErrorResponse, e:
	# 	# return 'Error: %s\n' % str(e)
	# 	return 'sfsfd'
	# return ''


	if request.GET:

		# request_token_key = request.GET['oauth_token']
		# if not request_token_key:
		# 	return "Expected a request token key back!"
		# request_token = TOKEN_STORE[request_token_key]
		# try:
		# 	access_token = sess.obtain_access_token(request_token)
		# 	TOKEN_STORE[access_token.key] = access_token
		# except rest.ErrorResponse, e:
		# 	return str(e)
		
		blah.append(request_token)
		# sess = session.DropboxSession(DROPBOX_APP_KEY, DROPBOX_APP_SECRET, ACCESS_TYPE)
		# request_token = sess.obtain_request_token()

		# try:
		# 	token = sess.obtain_access_token(request_token)
		# 	return "Token key: %s\nToken secret: %s" % (token.key, token.secret)
		# except rest.ErrorResponse, e:
		# 	return 'Error: %s\n' % str(e)
		# return ''
		# cl = client.DropboxClient(sess)
		# acct = cl.account_info()
		# return acct

		
		try:
			d = Dropbox.objects.get(user=user_obj)
			d.request_token = request.GET['oauth_token']
			d.dropbox_user_id = request.GET['uid']
			d.access_token = token
			d.save()
		except Dropbox.DoesNotExist:
			d = Dropbox()
			d.request_token = request.GET['oauth_token']
			d.dropbox_user_id = request.GET['uid']
			# d.access_token = token
			d.user = user_obj
			d.save()

	return render(request, 'dropboxapi/initialize.html',{'url':url})


'''OLD STUFFF'''
# def initialize(request, user_id):
# 	return render(request, 'dropboxapi/initialize.html',{'user_id':user_id})

# def ajax_dropbox_authorize(request):
# 	if request.POST:
# 		username = request.POST['username']
# 		password = request.POST['password']

# 		# d = Dropbox()


# 		# Configuring a session object
# 		# sess = session.DropboxSession(DROPBOX_APP_KEY, DROPBOX_APP_SECRET, ACCESS_TYPE)
# 		# request_token = sess.obtain_request_token()
		
# 		# Page that dropbox will redirect to on successful authentication
# 		redirect_url = 'http://localhost:7000/library/1/'
# 		sess = d.get_session()
# 		request_token = d.connect(sess)
# 		url = sess.build_authorize_url(request_token,redirect_url)
# 		user_obj = User.objects.get(id=request.POST['user_id'])

		
# 		d.session = sess
# 		d.request_token = request_token
# 		d.user = user_obj

# 		d.save()
# 		return HttpResponseRedirect(url)
# 	else:
# 		return HttpResponse()