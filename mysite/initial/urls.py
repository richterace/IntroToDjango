from django.urls import path

from . import views #import fro mthe directory we are in

urlpatterns = [
    path("", views.index, name="index"),
    path("v1/", views.v1, name="v1"),
]