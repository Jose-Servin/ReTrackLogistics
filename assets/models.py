from uuid import uuid4
from django.db import models
from clients.models import Client


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
