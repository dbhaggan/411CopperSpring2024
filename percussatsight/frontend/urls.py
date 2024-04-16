from django.urls import path, include
from .views import *
from rest_framework import routers

router = routers.DefaultRouter()

router.register(r'user', userViewSet, 'user')
router.register(r'instrument', instrumentViewSet, 'instrument')

urlpatterns = [
    path("api/", include(router.urls)),
    #path("api", include('rest_framework.urls')),
]

