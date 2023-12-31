from django.db import models
from django.core.validators import URLValidator, MaxLengthValidator


class Profile(models.Model):
    name = models.CharField(max_length=100, blank=False)
    github = models.URLField(
        validators=[URLValidator(), MaxLengthValidator(limit_value=500)],
        blank=False
    )
    linkedin = models.URLField(
        validators=[URLValidator(), MaxLengthValidator(limit_value=500)],
        blank=False
    )
    bio = models.TextField(
        validators=[MaxLengthValidator(limit_value=500)],
        blank=False
    )

    def __str__(self):
        return self.name


class Project(models.Model):
    name = models.CharField(max_length=50, blank=False)
    description = models.TextField(max_length=500, blank=False)
    github_url = models.URLField(
        validators=[URLValidator(), MaxLengthValidator(limit_value=500)],
        blank=False
    )
    keyword = models.CharField(max_length=50, blank=False)
    key_skill = models.CharField(max_length=50, blank=False)
    profile = models.ForeignKey(
        Profile,
        on_delete=models.CASCADE,
        related_name='projects'
    )

    def __str__(self):
        return self.name


class CertifyingInstitution(models.Model):
    name = models.CharField(max_length=100, blank=False)
    url = models.URLField(
        blank=False,
        validators=[URLValidator(), MaxLengthValidator(limit_value=500)],
        )

    def __str__(self):
        return self.name


class Certificate(models.Model):
    name = models.CharField(max_length=100, blank=False)
    certifying_institution = models.ForeignKey(
        CertifyingInstitution,
        on_delete=models.CASCADE,
        related_name='certificates',
        )
    timestamp = models.DateTimeField(auto_now_add=True)
    profiles = models.ManyToManyField(Profile, related_name='certificates')

    def __str__(self):
        return self.name
