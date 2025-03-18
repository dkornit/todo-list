from django.urls import path

from app.views import (TaskListView,
                       TaskCreateView,
                       TaskUpdateView,
                       TaskDeleteView,
                       TagListView,
                       TagCreateView,
                       TagUpdateView,
                       TagDeleteView,
                       CompleteTaskView,
                       UndoTaskView,
                       )

app_name = "app"



urlpatterns = [
    path("", TaskListView.as_view(), name="task-list"),
    path("create/", TaskCreateView.as_view(), name="task-create"),
    path("update/<int:pk>/", TaskUpdateView.as_view(), name="task-update"),
    path("delete/<int:pk>/", TaskDeleteView.as_view(), name="task-delete"),
    path("tags/", TagListView.as_view(), name="tag-list"),
    path("tags/create/", TagCreateView.as_view(), name="tag-create"),
    path("tags/update/<int:pk>/", TagUpdateView.as_view(), name="tag-update"),
    path("tags/delete/<int:pk>/", TagDeleteView.as_view(), name="tag-delete"),
    path("task/<int:task_id>/complete/", CompleteTaskView.as_view(), name="complete-task"),
    path("task/<int:task_id>/undo/", UndoTaskView.as_view(), name="undo-task"),
]
