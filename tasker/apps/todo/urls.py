from django.conf.urls.defaults import url, patterns
from django.contrib.auth.decorators import login_required
from django.views.generic import ListView

from todo.models import Task

urlpatterns = patterns('todo.views',
    url(r'^$', login_required(ListView.as_view(model=Task)), name='list'),
    url(r'^create/$', 'TaskCreateView', name='create'),
    url(r'^detail/(?P<identifier>\d+)/$', 'TaskDetailView', name='detail'),
    url(r'^edit/(?P<identifier>\d+)/$', 'TaskEditView', name='edit'),
    url(r'^close/(?P<identifier>\d+)/$', 'TaskCloseView', name='close'),
)
