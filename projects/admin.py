from django.contrib import admin
from projects.models import (
    Profile,
    Project,
    CertifyingInstitution,
    Certificate,
    )

admin.site.register(Profile)
admin.site.register(Project)
admin.site.register(Certificate)
admin.site.register(CertifyingInstitution)
