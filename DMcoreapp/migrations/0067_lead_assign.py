# Generated by Django 4.1.7 on 2023-06-21 15:03

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ("DMcoreapp", "0066_delete_lead_assign"),
    ]

    operations = [
        migrations.CreateModel(
            name="Lead_assign",
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
                ("telecaller", models.CharField(blank=True, max_length=255, null=True)),
                (
                    "checkbox",
                    models.ForeignKey(
                        blank=True,
                        null=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        to="DMcoreapp.all_leads",
                    ),
                ),
            ],
        ),
    ]
