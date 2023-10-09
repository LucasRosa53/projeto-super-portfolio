from rest_framework import routers
from django.urls import path, include
from .views import ProfileViewSet


router = routers.DefaultRouter()
router.register("profiles", ProfileViewSet)

urlpatterns = [
    path("", include(router.urls)),
]