from django.contrib.auth.models import AbstractUser
from django.db import models
from django.core.exceptions import ValidationError

class EmailAddress(models.Model):
    email = models.EmailField(unique=True)  # Unicità generale per sicurezza
    verified = models.BooleanField(default=False)

    def clean(self):
        """
        Controlla se esiste già un'email verificata con lo stesso indirizzo.
        """
        if self.verified and EmailAddress.objects.filter(email=self.email, verified=True).exclude(pk=self.pk).exists():
            raise ValidationError("Un'email verificata con questo indirizzo esiste già.")

    def save(self, *args, **kwargs):
        """
        Applica la validazione prima di salvare l'oggetto.
        """
        self.clean()  # Esegue la validazione
        super().save(*args, **kwargs)

    def __str__(self):
        return f"{self.email} (Verificata: {self.verified})"
        
class CustomUser(AbstractUser):
    """Custom user model to be extended in the future."""
    # Aggiungi qui i campi personalizzati
    pass
