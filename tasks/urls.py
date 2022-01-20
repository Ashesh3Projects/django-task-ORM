from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path("admin", admin.site.urls),
    path("", views.index),
    path("all_tasks/", views.all_tasks_view),
    path("tasks/", views.pending_tasks_view),
    path("completed_tasks/", views.completed_tasks_view),
    path("add-task/", views.add_task_view),
    path("delete-task/<int:task_id>/", views.delete_task),
    path("complete_task/<int:task_id>/", views.complete_task),
]
