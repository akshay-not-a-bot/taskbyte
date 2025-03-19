from django.contrib import admin
from django.urls import path, include
from todo_list_app import views as todo_views

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", todo_views.index, name="index"),
    path("todolist/", include("todo_list_app.urls")),
    path("about", todo_views.about, name="about"),
    path("account/", include("users_app.urls")),
]
