from django.contrib.auth.models import AbstractUser
from django.db import models

class CustomUser(AbstractUser):
    """Custom user model to be extended in the future."""
    # Aggiungi qui i campi personalizzati
    pass