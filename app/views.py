from django.shortcuts import redirect, get_object_or_404
from django.urls import reverse_lazy
from django.views import generic, View
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


class TaskStatusUpdateView(View):
    status = None

    def post(self, request, task_id):
        task = get_object_or_404(Task, id=task_id)
        task.is_done = self.status
        task.save()
        return redirect("app:task-list")

class CompleteTaskView(TaskStatusUpdateView):
    status = True

class UndoTaskView(TaskStatusUpdateView):
    status = False