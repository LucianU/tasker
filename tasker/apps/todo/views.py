from django.http import HttpResponseRedirect
from django.views.generic import ListView, DetailView, UpdateView, CreateView
from django.core.exceptions import PermissionDenied

from todo.models import Task
from todo.forms import TaskForm

class TaskListView(ListView):
    def get_queryset(self):
        if 'completed' in self.request.GET:
            return self.request.user.tasks.filter(
                    completed=self.request.GET['completed']
            )
        else:
            return self.request.user.tasks.all()

class TaskCreateView(CreateView):
    model = Task
    form_class = TaskForm

    def form_valid(self, form):
        self.object = form.save(commit=False)
        self.object.user = self.request.user
        self.object.save()

        return HttpResponseRedirect(self.get_success_url())

class TaskDetailView(DetailView):
    model = Task

    def get_object(self, *args, **kwargs):
        task = super(TaskDetailView, self).get_object(*args, **kwargs)

        if task.user != self.request.user:
            raise PermissionDenied

        return task

class TaskUpdateView(UpdateView):
    model = Task
    form_class = TaskForm

    def get_object(self, *args, **kwargs):
        task = super(TaskUpdateView, self).get_object(*args, **kwargs)

        if task.user != self.request.user:
            raise PermissionDenied

        return task
