from django.conf.urls.defaults import *
from django.views.generic.simple import direct_to_template


from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Example:
    # (r'^eportfoliodemo/', include('eportfoliodemo.foo.urls')),

    (r'^$', direct_to_template, { 'template': 'index.html' }),
    (r'^library/', include('eportfoliodemo.library.urls')),
    (r'^admin/doc/', include('django.contrib.admindocs.urls')),
    (r'^admin/', include(admin.site.urls)),
    (r'^accounts/login/$', 'django.contrib.auth.views.login'),
    (r'^accounts/logout/$', 'django.contrib.auth.views.logout'),
)
