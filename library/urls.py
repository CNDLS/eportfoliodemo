from django.conf.urls.defaults import *

urlpatterns = patterns('',
    (r'^(?P<user_id>\d+)$', 'library.views.show')
)