from django.urls import path

from . import views #import fro mthe directory we are in

urlpatterns = [
    path("<int:id>", views.index, name="index"),
    path("", views.home,name="home"),
]