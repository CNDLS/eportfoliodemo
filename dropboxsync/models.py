from django.db import models
from django.contrib.auth.models import User

# Dropbox essentials
from eportfoliodemo.settings import DROPBOX_APP_KEY, DROPBOX_APP_SECRET, DROPBOX_ACCESS_TYPE
from dropbox.client import DropboxClient
from dropbox import client, rest, session

class Dropbox(models.Model):
	folder_name = models.CharField(max_length=250)
	created = models.DateTimeField(auto_now_add=True)
	modified = models.DateTimeField(auto_now=True)
	# Save the user id of thw dropbox owner
	owner = models.ForeignKey(User)
	dropbox_user_id = models.IntegerField(blank=True, null=True)
	size = models.CharField(max_length=10)

	def __unicode__(self):
		return self.folder_name

	def connect(self, request_token, sess):
		
		# User needs to "allow" this url for dropbox to access the app folder
		url = sess.build_authorize_url(request_token)
		return url

	def account_info(self, request_token, sess):
		from dropbox import client
		client = client.DropboxClient(sess)
		account_info = client.account_info()
		return account_info

	def get_files(self, request_token, sess):
		return files

	def get_folders(self, request_token, sess):
		return folders
	


