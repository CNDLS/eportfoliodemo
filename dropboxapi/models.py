from django.db import models
from django.contrib.auth.models import User
from settings import DROPBOX_APP_KEY, DROPBOX_APP_SECRET, ACCESS_TYPE
'''
Import Dropbox library and the respective settings
'''
# Dropbox SDK
from dropbox.session import DropboxSession
from dropbox.client import DropboxClient
from dropbox import client, rest, session

# Create your models here.
class Dropbox(models.Model):
	created = models.DateTimeField(auto_now_add=True)
	modified = models.DateTimeField(auto_now_add=True)
	dropbox_user_id = models.IntegerField(blank=True,null=True)
	user = models.ForeignKey(User,unique=True)
	request_token = models.CharField(max_length=200, blank=True, null=True)
	access_token = models.CharField(max_length=200, blank=True, null=True)

	def get_session(self):
		sess = session.DropboxSession(DROPBOX_APP_KEY, DROPBOX_APP_SECRET, ACCESS_TYPE)
		return sess

	def connect(self,sess):
		request_token = sess.obtain_request_token()
		return request_token

	def get_access_token(self,sess, request_token):
		access_token = sess.obtain_access_token(request_token)
		return access_token


# TOKEN_STORE = {}

# def get_session():
#     return session.DropboxSession(DROPBOX_APP_KEY, DROPBOX_APP_SECRET, ACCESS_TYPE)

# class DropboxHandler():
# 	def get_url(self):
# 		sess = get_session()
# 		request_token = sess.obtain_request_token()
# 		TOKEN_STORE[request_token.key] = request_token
# 		callback = 'http://localhost:7000/library/1/'
# 		url = sess.build_authorize_url(request_token, oauth_callback=callback)
# 		return url

# 	def callback_page(self, oauth_token=None):
# 		request_token_key = oauth_token
# 		if not request_token_key:
# 			return "Expected a request token key back!"

#         sess = get_session()
#         request_token = TOKEN_STORE[request_token_key]
#         access_token = sess.obtain_access_token(request_token)
#         TOKEN_STORE[access_token.key] = access_token

#         self.set_cookie('access_token_key', access_token.key)
##### TODO: ADD access_token in the db with user info! This is important so that the user does not have keep authenticating in dropbox.com