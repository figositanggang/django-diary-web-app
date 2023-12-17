from django.urls import path

from . import views

app_name = "diary"

urlpatterns = [
    path("", views.index, name="index"),
    path("create/", views.create, name="create"),
    path("diary/<int:pk>", views.detail, name="detail"),
]
