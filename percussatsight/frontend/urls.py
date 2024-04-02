from django.urls import path, include
from .views import *
from rest_framework import routers

router = routers.DefaultRouter()

router.register(r'user', userViewSet, 'user')
router.register(r'instrument', instrumentViewSet, 'instrument')

urlpatterns = [
    path("home", homepage, name="home"),
    path("sheets", sheetspage, name="sheets"),
    path("", loginpage, name="login"),
    path("signup", signuppage, name="signup"),
    path("api/", include(router.urls)),
    path("practice", practicepage, name="practice"),
    #path("api", include('rest_framework.urls')),
]

