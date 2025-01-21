from django.db import models
from django.core.validators import RegexValidator, EmailValidator
from uuid import uuid4


class Client(models.Model):

    name = models.CharField(max_length=255, verbose_name="Client Name")
    email = models.EmailField(
        max_length=255, unique=True, validators=[EmailValidator()]
    )
    phone_number = models.CharField(max_length=20, blank=True, null=True)
    address = models.CharField(max_length=255, blank=True, null=True)
    city = models.CharField(max_length=100, blank=True, null=True)
    state = models.CharField(max_length=100, blank=True, null=True)
    zipcode = models.CharField(
        max_length=20,
        blank=True,
        null=True,
        validators=[
            RegexValidator(
                regex=r"^\d{5}(-\d{4})?$",
                message="Enter a valid ZIP code (e.g., 12345 or 12345-6789).",
            )
        ],
    )
    country = models.CharField(max_length=100, blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = "Client"
        verbose_name_plural = "Clients"
        indexes = [
            models.Index(fields=["name"]),
            models.Index(fields=["email"]),
        ]

    def __str__(self):
        return self.name


class ClientContact(models.Model):
    """
    Represents a contact person associated with a client.
    """

    client = models.ForeignKey(
        Client, on_delete=models.CASCADE, related_name="contacts"
    )
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    email = models.EmailField(
        max_length=255, unique=True, validators=[EmailValidator()]
    )
    phone_number = models.CharField(max_length=20, blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = "Client Contact"
        verbose_name_plural = "Client Contacts"
        indexes = [
            models.Index(fields=["first_name"]),
            models.Index(fields=["last_name"]),
            models.Index(fields=["email"]),
        ]

    def __str__(self):
        return f"{self.first_name} {self.last_name} from ({self.client.name})"


class Asset(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()
    industry = models.CharField(max_length=255)
    owner = models.ForeignKey(Client, on_delete=models.PROTECT, related_name="assets")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name


class Tracker(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid4)
    name = models.CharField(max_length=255)
    description = models.TextField()
    asset = models.ForeignKey(Asset, on_delete=models.PROTECT, related_name="trackers")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    sensor_data = models.JSONField(null=True, blank=True)

    STATUS_ACTIVE = "Y"
    STATUS_INACTIVE = "N"

    STATUS_CHOICES = [(STATUS_ACTIVE, "Active"), (STATUS_INACTIVE, "Inactive")]
    status = models.CharField(
        max_length=1, choices=STATUS_CHOICES, default=STATUS_ACTIVE
    )

    def __str__(self):
        return self.name
