from django.shortcuts import redirect
from django.urls import reverse_lazy
from django.views import generic
from app.models import Task, Tag


class TaskListView(generic.ListView):
    model = Task


class TaskCreateView(generic.CreateView):
    model = Task
    fields = "__all__"
    success_url = reverse_lazy("app:task-list")


class TaskUpdateView(generic.UpdateView):
    model = Task
    fields = "__all__"
    success_url = reverse_lazy("app:task-list")


class TaskDeleteView(generic.DeleteView):
    model = Task
    success_url = reverse_lazy("app:task-list")


class TagListView(generic.ListView):
    model = Tag


class TagCreateView(generic.CreateView):
    model = Tag
    fields = "__all__"
    success_url = reverse_lazy("app:task-list")


class TagUpdateView(generic.UpdateView):
    model = Tag
    fields = "__all__"
    success_url = reverse_lazy("app:task-list")


class TagDeleteView(generic.DeleteView):
    model = Tag
    success_url = reverse_lazy("app:task-list")



def complete_task(request, task_id):
    task = Task.objects.get(id=task_id)
    task.is_done = True
    task.save()
    return redirect("todo_app:task-list")


def undo_task(request, task_id):
    task = Task.objects.get(id=task_id)
    task.is_done = False
    task.save()
    return redirect("todo_app:task-list")