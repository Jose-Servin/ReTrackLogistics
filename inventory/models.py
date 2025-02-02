from django.db import models
from registry.models import Client


class Asset(models.Model):
    MANUFACTURING = "Manufacturing"
    AUTOMOTIVE = "Automotive"
    PHARMACEUTICAL = "Pharmaceutical"
    LOGISTICS = "Logistics"
    ELECTRONICS = "Electronics"
    OIL_AND_GAS = "Oil and Gas"

    INDUSTRY_CHOICES = [
        (MANUFACTURING, "Manufacturing"),
        (AUTOMOTIVE, "Automotive"),
        (PHARMACEUTICAL, "Pharmaceutical"),
        (LOGISTICS, "Logistics"),
        (ELECTRONICS, "Electronics"),
        (OIL_AND_GAS, "Oil and Gas"),
    ]

    name = models.CharField(max_length=255)
    description = models.TextField()
    industry = models.CharField(max_length=255, choices=INDUSTRY_CHOICES)
    owner = models.ForeignKey(Client, on_delete=models.PROTECT, related_name="assets")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name
