# Generated by Django 5.0.3 on 2025-01-11 16:08

import django.core.validators
import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Client",
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
                ("name", models.CharField(max_length=255, verbose_name="Client Name")),
                ("email", models.EmailField(max_length=255, unique=True)),
                (
                    "phone_number",
                    models.CharField(blank=True, max_length=20, null=True),
                ),
                ("address", models.CharField(blank=True, max_length=255, null=True)),
                ("city", models.CharField(blank=True, max_length=100, null=True)),
                ("state", models.CharField(blank=True, max_length=100, null=True)),
                (
                    "zipcode",
                    models.CharField(
                        blank=True,
                        max_length=20,
                        null=True,
                        validators=[
                            django.core.validators.RegexValidator(
                                message="Enter a valid ZIP code (e.g., 12345 or 12345-6789).",
                                regex="^\\d{5}(-\\d{4})?$",
                            )
                        ],
                    ),
                ),
                ("country", models.CharField(blank=True, max_length=100, null=True)),
                ("created_at", models.DateTimeField(auto_now_add=True)),
                ("updated_at", models.DateTimeField(auto_now=True)),
            ],
            options={
                "verbose_name": "Client",
                "verbose_name_plural": "Clients",
                "indexes": [
                    models.Index(fields=["name"], name="clients_cli_name_5ab7bc_idx"),
                    models.Index(fields=["email"], name="clients_cli_email_56b9fc_idx"),
                ],
            },
        ),
        migrations.CreateModel(
            name="ClientContact",
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
                ("first_name", models.CharField(max_length=255)),
                ("last_name", models.CharField(max_length=255)),
                ("email", models.EmailField(max_length=255, unique=True)),
                (
                    "phone_number",
                    models.CharField(blank=True, max_length=20, null=True),
                ),
                ("created_at", models.DateTimeField(auto_now_add=True)),
                ("updated_at", models.DateTimeField(auto_now=True)),
                (
                    "client",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="contacts",
                        to="clients.client",
                    ),
                ),
            ],
            options={
                "verbose_name": "Client Contact",
                "verbose_name_plural": "Client Contacts",
                "indexes": [
                    models.Index(
                        fields=["first_name"], name="clients_cli_first_n_877bff_idx"
                    ),
                    models.Index(
                        fields=["last_name"], name="clients_cli_last_na_008d07_idx"
                    ),
                    models.Index(fields=["email"], name="clients_cli_email_030d36_idx"),
                ],
            },
        ),
    ]
