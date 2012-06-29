

from django.conf import settings
from django.core.management import setup_environ

import settings as settings_mod
setup_environ(settings_mod)

from django.db import models
from django.contrib.auth.models import User
from dropboxsync.models import Dropbox
from eportfoliodemo.settings import DROPBOX_APP_KEY, DROPBOX_APP_SECRET, DROPBOX_ACCESS_TYPE
from dropbox import client, rest, session


sess = session.DropboxSession(DROPBOX_APP_KEY, DROPBOX_APP_SECRET, DROPBOX_ACCESS_TYPE)
request_token = sess.obtain_request_token()

# d = Dropbox()
# url = d.connect(request_token, sess)
# print "url:", url
# print "Please authorize in the browser. After you're done, press enter."
# raw_input()

# access_token = sess.obtain_access_token(request_token)

# acct = d.account_info(request_token,sess)
# print acct