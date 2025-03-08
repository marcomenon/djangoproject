from django.contrib.auth.models import AbstractUser
from django.db import models
from django.core.exceptions import ValidationError
from allauth.account.models import EmailAddress as AllauthEmailAddress

class EmailAddress(AllauthEmailAddress):
    class Meta:
        app_label = "accounts"  # Indica che appartiene alla tua app
        managed = True  # Django gestirà il modello
        unique_together = ("email", "verified")  # Evita duplicati verificati manualmente

    def clean(self):
        """
        Controlla se esiste già un'email verificata con lo stesso indirizzo.
        MariaDB non supporta UNIQUE con condizioni, quindi validiamo manualmente.
        """
        if self.verified and EmailAddress.objects.filter(email=self.email, verified=True).exclude(pk=self.pk).exists():
            raise ValidationError("Un'email verificata con questo indirizzo esiste già.")

    def save(self, *args, **kwargs):
        self.clean()  # Esegue la validazione prima di salvare
        super().save(*args, **kwargs)

    def __str__(self):
        return f"{self.email} (Verificata: {self.verified})"

class CustomUser(AbstractUser):
    """Custom user model to be extended in the future."""
    pass
