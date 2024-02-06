from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("home", views.homepage, name="home"),
    path("sheets", views.sheetspage, name="sheets"),
    path("sheets", views.sheetspage, name="sheets"),
    path("login", views.login, name="login"),
    path("signup", views.signup, name="signup"),
]

