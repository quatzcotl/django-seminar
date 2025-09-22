from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    """Unser eigenes User-Modell."""

    address = models.CharField(max_length=200)
