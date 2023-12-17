from django.urls import path
from django.contrib.auth import views as auth_views

from . import views
from . import forms

app_name = "user"

urlpatterns = [
    path(
        "login/",
        auth_views.LoginView.as_view(
            authentication_form=forms.LoginForm, template_name="user/login.html"
        ),
        name="login",
    ),
    path("signup/", views.signup, name="signup"),
    path("logout/", views.logout_view, name="logout"),
]
