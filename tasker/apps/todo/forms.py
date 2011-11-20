from django import forms

from todo.models import Task

class TaskForm(forms.ModelForms):
    class Meta:
        model = Task
