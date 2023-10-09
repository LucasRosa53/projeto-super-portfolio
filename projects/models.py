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
