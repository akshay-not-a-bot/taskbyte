from users_app import views
from django.urls import path

urlpatterns = [
    path("", views.account, name="account"),
    path("register", views.register, name="register"),
    # path("login", views.login, name="login"),
    # path("logout", views.logout, name="logout"),
]
