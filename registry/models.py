from django.db import models
from django.core.validators import EmailValidator
from core.validators import validate_phone_number, validate_zip_code


class Client(models.Model):

    name = models.CharField(max_length=255, verbose_name="Client Name")
    email = models.EmailField(
        max_length=255, unique=True, validators=[EmailValidator()]
    )
    phone_number = models.CharField(
        max_length=20,
        validators=[validate_phone_number],
    )
    address = models.CharField(max_length=255, blank=True, null=True)
    city = models.CharField(max_length=100, blank=True, null=True)
    state = models.CharField(max_length=100, blank=True, null=True)
    zipcode = models.CharField(
        max_length=20,
        blank=True,
        null=True,
        validators=[validate_zip_code],
    )
    country = models.CharField(max_length=100, blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name


class Contact(models.Model):
    """
    Represents a contact person associated with a client.
    """

    client = models.ForeignKey(
        Client,
        on_delete=models.PROTECT,
        related_name="contacts",
    )
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    email = models.EmailField(
        max_length=255, unique=True, validators=[EmailValidator()]
    )
    phone_number = models.CharField(
        max_length=20,
        validators=[validate_phone_number],
    )
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.first_name} {self.last_name} from ({self.client.name})"
