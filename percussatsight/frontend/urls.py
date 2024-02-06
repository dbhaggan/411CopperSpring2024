from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("home", views.homepage, name="home"),
<<<<<<< HEAD
    path("sheets", views.sheetspage, name="sheets")
]
=======
    path("sheets", views.sheetspage, name="sheets"),
    path("login", views.login, name="login"),
    path("signup", views.signup, name="signup"),
]
>>>>>>> f4d0010e3d15b7681c82a7b4e5fa078e66766571
