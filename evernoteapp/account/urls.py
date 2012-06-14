from django.conf.urls.defaults import patterns, url

urlpatterns = patterns('',
    url('^logout/$', 'eportfoliodemo.evernoteapp.account.views.logout_page'),
    url('^auth/$', 'eportfoliodemo.evernoteapp.account.views.auth'),
)

