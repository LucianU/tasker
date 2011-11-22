from django.conf.urls.defaults import url, patterns
from django.contrib.auth.decorators import login_required

from todo.views import (TaskListView, TaskCreateView, TaskDetailView,
                        TaskUpdateView)

urlpatterns = patterns('',
    url(r'^$', login_required(TaskListView.as_view()), name='list'),
    url(r'^create/$',
        login_required(TaskCreateView.as_view()),
        name='create'),
    url(r'^detail/(?P<pk>\d+)/$',
        login_required(TaskDetailView.as_view()),
        name='detail'),
    url(r'^edit/(?P<pk>\d+)/$',
        login_required(TaskUpdateView.as_view()),
        name='edit'),
)
