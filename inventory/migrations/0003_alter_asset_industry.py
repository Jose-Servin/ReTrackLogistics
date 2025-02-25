# Generated by Django 5.0.3 on 2025-02-02 17:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("inventory", "0002_alter_asset_industry"),
    ]

    operations = [
        migrations.AlterField(
            model_name="asset",
            name="industry",
            field=models.CharField(
                choices=[
                    ("Manufacturing", "Manufacturing"),
                    ("Automotive", "Automotive"),
                    ("Pharmaceutical", "Pharmaceutical"),
                    ("Logistics", "Logistics"),
                    ("Electronics", "Electronics"),
                    ("Oil and Gas", "Oil and Gas"),
                ],
                max_length=255,
            ),
        ),
    ]
