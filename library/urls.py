from django.conf.urls.defaults import *

urlpatterns = patterns('',
    url(r'^(?P<user_id>\d+)$', 'library.views.show')
)