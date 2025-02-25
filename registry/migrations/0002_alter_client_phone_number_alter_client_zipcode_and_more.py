# Generated by Django 5.0.3 on 2025-01-24 22:25

import core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("registry", "0001_initial"),
    ]

    operations = [
        migrations.AlterField(
            model_name="client",
            name="phone_number",
            field=models.CharField(
                blank=True,
                max_length=20,
                null=True,
                validators=[core.validators.validate_phone_number],
            ),
        ),
        migrations.AlterField(
            model_name="client",
            name="zipcode",
            field=models.CharField(
                blank=True,
                max_length=20,
                null=True,
                validators=[core.validators.validate_zip_code],
            ),
        ),
        migrations.AlterField(
            model_name="contact",
            name="phone_number",
            field=models.CharField(
                blank=True,
                max_length=20,
                null=True,
                validators=[core.validators.validate_phone_number],
            ),
        ),
    ]
