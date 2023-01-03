from django.urls import path

from . import views

urlpatterns = [
    path("index", views.index, name="index"),
    path("create", views.create, name="create"),
    path("update", views.update, name="update"),
    path("details", views.details, name="details"),
    path("delete", views.delete, name="delete"),
]
