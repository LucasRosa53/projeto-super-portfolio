from rest_framework import routers
from django.urls import path, include
from .views import (
    ProfileViewSet,
    ProjectViewSet,
    CertificateViewSet,
    CertifyingInstitutionViewSet,
)

router = routers.DefaultRouter()
router.register("profiles", ProfileViewSet)
router.register("projects", ProjectViewSet)
router.register("projects/<int:id>", ProjectViewSet)
router.register("certificates", CertificateViewSet)
router.register("certifying-institutions", CertifyingInstitutionViewSet)

urlpatterns = [
    path("", include(router.urls)),
]
