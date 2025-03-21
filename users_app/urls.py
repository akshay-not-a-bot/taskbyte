from users_app import views
from django.urls import path
from django.contrib.auth import views as auth_views

urlpatterns = [
    path("", views.account, name="account"),
    path("register", views.register, name="register"),
    # using Django's class views for login and logout, also stating template name so it doesn't look for temp in default path: templates\registration\login.html
    path(
        "login", auth_views.LoginView.as_view(template_name="login.html"), name="login"
    ),
    path(
        "logout",
        auth_views.LogoutView.as_view(template_name="logout.html"),
        name="logout",
    ),
    path(
        "pswd_change",
        auth_views.PasswordChangeView.as_view(template_name="pswd_change.html"),
        name="pswd_change",
    ),
    path(
        "pswd_done",
        auth_views.PasswordChangeDoneView.as_view(template_name="pswd_done.html"),
        name="pswd_done",
    ),
]
