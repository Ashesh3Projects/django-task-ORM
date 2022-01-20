from typing import List
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render

from tasks.models import Task


def index(request):
    return render(request, "index.html")


def all_tasks_view(request):
    return render(
        request,
        "all.html",
        {
            "pending_tasks": Task.objects.all().filter(completed=False, deleted=False),
            "completed_tasks": Task.objects.all().filter(completed=True, deleted=False),
        },
    )


def pending_tasks_view(request):
    return render(request, "pending.html", {"tasks": Task.objects.all().filter(completed=False, deleted=False)})


def completed_tasks_view(request):
    return render(request, "completed.html", {"tasks": Task.objects.all().filter(completed=True, deleted=False)})


def add_task_view(request):
    task = request.GET.get("task")
    if task:
        Task(title=task).save()
        return HttpResponseRedirect("/tasks")
    else:
        return render(request, "add.html")


def complete_task(request, task_id):
    Task.objects.filter(id=task_id).update(completed=True)
    return HttpResponseRedirect("/tasks")


def delete_task(request, task_id):
    Task.objects.filter(id=task_id).update(deleted=True)
    return HttpResponseRedirect("/tasks")
