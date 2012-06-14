from django.conf.urls.defaults import patterns, include, url
from settings import MEDIA_ROOT
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    url('^$', 'eportfoliodemo.evernoteapp.account.views.home_page'),
    url(r'^login/$', 'eportfoliodemo.evernoteapp.account.views.login_page' ),
    url('^home/$', 'eportfoliodemo.evernoteapp.basic.views.landing'),
    url('^post_token/$', 'eportfoliodemo.evernoteapp.basic.views.post_evernote_token'),
    url('^auth/gettok/$', 'eportfoliodemo.evernoteapp.basic.views.run_evernote_auth'),
    url('^auth/usertok/$', 'eportfoliodemo.evernoteapp.basic.views.get_evernote_token'),
    url(r'^static/(?P<path>.*)$', 'django.views.static.serve',
        {'document_root': MEDIA_ROOT}),
    url(r'^account/', include('eportfoliodemo.evernoteapp.account.urls')),
    url(r'^admin/', include(admin.site.urls)),
)
