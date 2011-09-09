from django.conf.urls.defaults import *

urlpatterns = patterns('',
    (r'^(?P<user_id>\d+)$', 'eportfoliodemo.library.views.show')
)