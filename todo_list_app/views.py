from django.shortcuts import render, redirect
from .models import TaskList
from .forms import TaskForm
from django.contrib import messages
from django.core.paginator import Paginator  # importing Paginator class
from django.contrib.auth.decorators import login_required

# login_required is used to add logged in only restriction on page


@login_required
def todo_list(request):
    # for POST request
    if request.method == "POST":
        form = TaskForm(request.POST or None)
        if form.is_valid():  # making sure data is valid using inherited is_valid method
            instance = form.save(commit=False)
            # commit=False stops form to be saved in DB so we can assign it an owner ForeignKey
            instance.owner = request.user
            instance.save()
            messages.success(request, "New task added successfully!", extra_tags="add")
        return redirect("todo_list")
    # for GET request
    else:
        all_task = TaskList.objects.filter(owner=request.user)
        # fitering to show only the tasks which thr current user is owner of
        paginator = Paginator(all_task, 5)
        # instantiating, Paginator(object to paginate, max_items in a page)
        page = request.GET.get("pg")  # 'pg' is used in url to pass page number
        all_task = paginator.get_page(page)
        # assigning paginator view for 'page' to all_task obj, which we use next to render todo_list.html
        return render(request, "todo_list.html", {"all_task": all_task})


@login_required
def delete_task(request, task_id):
    task = TaskList.objects.get(pk=task_id)
    if task.owner == request.user:  # making sure only owner can access this func
        task.delete()
        messages.success(request, "Task deleted successfully!", extra_tags="delete")
    else:
        messages.error(request, "User acccess denied!")

    return redirect("todo_list")
    # TObe Done: redirect takes to the same page in pagination


@login_required
def edit_task(request, task_id):
    task = TaskList.objects.get(pk=task_id)
    if request.method == "POST":
        form = TaskForm(request.POST or None, instance=task)
        if form.is_valid():
            form.save()
            messages.success(request, "Task edited successfully!", extra_tags="edit")
        return redirect("todo_list")
    else:
        return render(request, "edit.html", {"task": task})


def index(request):
    context = {"index_msg": "Welcome to the Homepage!!!"}
    return render(request, "index.html", context)


def contact(request):
    context = {"contact_msg": "Hi, this is Contact Me page"}
    return render(request, "contact.html", context)


def about(request):
    context = {"about_msg": "Hi, this is About Me page"}
    return render(request, "about.html", context)
