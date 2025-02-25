# Generated by Django 5.0.3 on 2025-01-22 21:42

import django.db.models.deletion
import uuid
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ("inventory", "0001_initial"),
    ]

    operations = [
        migrations.CreateModel(
            name="Tracker",
            fields=[
                (
                    "id",
                    models.UUIDField(
                        default=uuid.uuid4,
                        editable=False,
                        primary_key=True,
                        serialize=False,
                    ),
                ),
                ("name", models.CharField(max_length=255)),
                ("description", models.TextField()),
                (
                    "tracker_type",
                    models.CharField(
                        choices=[
                            ("GPS", "GPS Tracker"),
                            ("TEMP", "Temperature Tracker"),
                            ("SHOCK", "Shock Detector"),
                        ],
                        default="GPS",
                        max_length=50,
                    ),
                ),
                ("created_at", models.DateTimeField(auto_now_add=True)),
                ("updated_at", models.DateTimeField(auto_now=True)),
                (
                    "status",
                    models.CharField(
                        choices=[("Y", "Active"), ("N", "Inactive")],
                        default="Y",
                        max_length=1,
                    ),
                ),
                (
                    "asset",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.PROTECT,
                        related_name="trackers",
                        to="inventory.asset",
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="SensorDataLog",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("timestamp", models.DateTimeField(auto_now_add=True)),
                ("sensor_data", models.JSONField()),
                (
                    "tracker",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.PROTECT,
                        related_name="sensor_logs",
                        to="tracking.tracker",
                    ),
                ),
            ],
            options={
                "ordering": ["-timestamp"],
            },
        ),
    ]
