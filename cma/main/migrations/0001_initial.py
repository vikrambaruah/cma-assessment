# Generated by Django 4.2.6 on 2023-10-21 13:24

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="OfficerData",
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
                ("company_number", models.CharField(max_length=20)),
                ("person_number", models.CharField(max_length=20)),
                (
                    "appointment_date",
                    models.CharField(blank=True, max_length=8, null=True),
                ),
                ("postcode", models.CharField(blank=True, max_length=10, null=True)),
                (
                    "date_of_birth",
                    models.CharField(blank=True, max_length=6, null=True),
                ),
                ("title", models.CharField(blank=True, max_length=255, null=True)),
                ("first_name", models.CharField(blank=True, max_length=255, null=True)),
                ("last_name", models.CharField(blank=True, max_length=255, null=True)),
                ("honours", models.CharField(blank=True, max_length=255, null=True)),
                ("care_of", models.CharField(blank=True, max_length=255, null=True)),
                ("po_box", models.CharField(blank=True, max_length=255, null=True)),
                ("address1", models.CharField(blank=True, max_length=255, null=True)),
                ("address2", models.CharField(blank=True, max_length=255, null=True)),
                ("town", models.CharField(blank=True, max_length=255, null=True)),
                ("county", models.CharField(blank=True, max_length=255, null=True)),
                ("country", models.CharField(blank=True, max_length=255, null=True)),
            ],
        ),
    ]
