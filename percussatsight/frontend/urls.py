from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("home", views.homepage, name="home"),
    path("sheets", views.sheetspage, name="sheets")
]
