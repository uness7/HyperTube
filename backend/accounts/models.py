from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    # Fields like username, first_name, last_name already included in since we inherit from AbstractUser.
    email = models.EmailField(unique=True)

    REQUIRED_FIELDS = [
            "first_name",
            "last_name",
            "email",
            "password",
    ]  # createsuperuser will require entering email field as well as first and last names.

    def __str__(self):
        return f"{self.username} ({self.email})"
