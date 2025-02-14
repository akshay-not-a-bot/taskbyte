from users_app import views
from django.urls import path, include

urlpatterns = [
    path("", views.landing, name="landing"),
]
