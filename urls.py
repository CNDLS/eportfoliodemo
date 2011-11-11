from django.conf.urls.defaults import *
from django.views.generic.simple import direct_to_template


from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Example:
    # (r'^eportfoliodemo/', include('eportfoliodemo.foo.urls')),

    (r'^$', direct_to_template, { 'template': 'index.html' }),
    (r'^assets/', include('eportfoliodemo.assets.urls')),
    (r'^assetaliases/', include('eportfoliodemo.assetaliases.urls')),
    (r'^profiles/', include('eportfoliodemo.profiles.urls')),
    (r'^library/', include('eportfoliodemo.library.urls')),
    (r'^libraryitems/', include('eportfoliodemo.libraryitems.urls')),
    (r'^folders/', include('eportfoliodemo.folders.urls')),
    (r'^collectionitems/', include('eportfoliodemo.collectionitems.urls')),
    (r'^collections/', include('eportfoliodemo.usercollections.urls')),
    (r'^reflect/', include('eportfoliodemo.reflections.urls')),
    (r'^present/', include('eportfoliodemo.present.urls')),
    (r'^admin/doc/', include('django.contrib.admindocs.urls')),
    (r'^admin/', include(admin.site.urls)),
    (r'^accounts/login/$', 'django.contrib.auth.views.login'),
    (r'^accounts/logout/$', 'django.contrib.auth.views.logout')
)
