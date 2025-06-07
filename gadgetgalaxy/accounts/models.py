from django.contrib.auth.models import AbstractUser
from django.db import models
import uuid
from django.utils import timezone
from datetime import timedelta


def get_default_activation_expiry():
    return timezone.now() + timedelta(days=1)

class CustomUser(AbstractUser):
    email = models.EmailField(unique=True)
    is_active = models.BooleanField(default=False)
    activation_token = models.UUIDField(default=uuid.uuid4)
    activation_expiry = models.DateTimeField(default=get_default_activation_expiry)


    def __str__(self):
        return self.username
