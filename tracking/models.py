from django.db import models
from uuid import uuid4
from inventory.models import Asset


class Tracker(models.Model):
    TRACKER_TYPE_CHOICES = [
        ("GPS", "GPS Tracker"),
        ("TEMP", "Temperature Tracker"),
        ("SHOCK", "Shock Detector"),
    ]

    id = models.UUIDField(primary_key=True, default=uuid4, editable=False)
    name = models.CharField(max_length=255)
    description = models.TextField()
    tracker_type = models.CharField(
        max_length=50, choices=TRACKER_TYPE_CHOICES, default="GPS"
    )
    asset = models.ForeignKey(Asset, on_delete=models.PROTECT, related_name="trackers")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    STATUS_ACTIVE = "Y"
    STATUS_INACTIVE = "N"

    STATUS_CHOICES = [
        (STATUS_ACTIVE, "Active"),
        (STATUS_INACTIVE, "Inactive"),
    ]
    status = models.CharField(
        max_length=1, choices=STATUS_CHOICES, default=STATUS_ACTIVE
    )

    def __str__(self):
        return f"{self.name}"


class SensorDataLog(models.Model):
    tracker = models.ForeignKey(
        Tracker, on_delete=models.PROTECT, related_name="sensor_logs"
    )
    timestamp = models.DateTimeField(auto_now_add=True)  # Log timestamp
    sensor_data = models.JSONField()  # Storing the sensor data as JSON

    class Meta:
        ordering = ["-timestamp"]  # Latest logs first for easier retrieval

    def __str__(self):
        return f"Log for {self.tracker.name} at {self.timestamp}"
