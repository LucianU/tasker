from django.conf.urls.defaults import patterns, include, url

from tastypie.api import Api
from todo.api import TaskResource

v1_api = Api(api_name='v1')
v1_api.register(TaskResource())

urlpatterns = patterns('',
    url(r'^', include('todo.urls', namespace='todo')),
    url(r'^accounts/', include('registration.urls')),
    url(r'^api/', include(v1_api.urls)),
)
