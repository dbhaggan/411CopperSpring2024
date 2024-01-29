from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("home", view.homepage, name="home"),
    path("sheets", view.sheetspage, name="sheets")
]
