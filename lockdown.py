###
# Copyright (c) 2006-2007, Jared Kuolt
# All rights reserved.
# 
# Redistribution and use in source and binary forms, with or without 
# modification, are permitted provided that the following conditions are met:
# 
#     * Redistributions of source code must retain the above copyright notice, 
#       this list of conditions and the following disclaimer.
#     * Redistributions in binary form must reproduce the above copyright 
#       notice, this list of conditions and the following disclaimer in the 
#       documentation and/or other materials provided with the distribution.
#     * Neither the name of the SuperJared.com nor the names of its 
#       contributors may be used to endorse or promote products derived from 
#       this software without specific prior written permission.
# 
# THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS "AS IS" 
# AND ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED TO, THE 
# IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE 
# ARE DISCLAIMED. IN NO EVENT SHALL THE COPYRIGHT OWNER OR CONTRIBUTORS BE 
# LIABLE FOR ANY DIRECT, INDIRECT, INCIDENTAL, SPECIAL, EXEMPLARY, OR 
# CONSEQUENTIAL DAMAGES (INCLUDING, BUT NOT LIMITED TO, PROCUREMENT OF 
# SUBSTITUTE GOODS OR SERVICES; LOSS OF USE, DATA, OR PROFITS; OR BUSINESS 
# INTERRUPTION) HOWEVER CAUSED AND ON ANY THEORY OF LIABILITY, WHETHER IN 
# CONTRACT, STRICT LIABILITY, OR TORT (INCLUDING NEGLIGENCE OR OTHERWISE) 
# ARISING IN ANY WAY OUT OF THE USE OF THIS SOFTWARE, EVEN IF ADVISED OF THE 
# POSSIBILITY OF SUCH DAMAGE.
###

from django.conf import settings
from django.contrib.auth.views import login
from django.http import HttpResponseRedirect
import re

class RequireLoginMiddleware(object):
    """
    Require Login middleware. If enabled, each Django-powered page will
    require authentication.
    
    If an anonymous user requests a page, he/she is redirected to the login
    page set by REQUIRE_LOGIN_PATH or /accounts/login/ by default.
    """
    def __init__(self):
       #self.require_login_path = getattr(settings, 'REQUIRE_LOGIN_PATH', '/accounts/login/') 
        self.require_login_path = '/accounts/login/'
        self.feed_path = '/feeds/latest/'
        self.inquiry_feed_path = '/feeds/inquiries/'

    def process_request(self, request):
        s = request.path
        
        m = re.search('/feeds/people/(.*)/', s)
        if m is None:
            #Not a match
            user_feeds = False
        else:
            #Match
            user_feeds = True

        m = re.search('/setup/(.*)/', s)
        if m is None:
            inquiry = False
        else:
            inquiry = True

        m = re.search('/api/(.*)/', s)
        if m is None:
            api_call = False
        else:
            api_call = True
            
        if request.path != self.require_login_path and request.path != self.feed_path and request.path != self.inquiry_feed_path and user_feeds != True and inquiry != True and api_call != True and request.user.is_anonymous():
            if request.POST:
                return login(request)
            else:
                return HttpResponseRedirect('%s?next=%s' % (self.require_login_path, request.path))
                
