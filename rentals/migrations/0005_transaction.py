# Generated by Django 5.0.7 on 2024-07-26 09:43

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("rentals", "0004_ticket"),
    ]

    operations = [
        migrations.CreateModel(
            name="Transaction",
            fields=[
                ("id", models.AutoField(primary_key=True, serialize=False)),
                ("transaction_date", models.DateTimeField()),
                (
                    "payment_method",
                    models.CharField(
                        choices=[("credit_card", "Credit Card"), ("paypal", "PayPal")],
                        max_length=100,
                    ),
                ),
                ("amount", models.DecimalField(decimal_places=2, max_digits=10)),
                (
                    "status",
                    models.CharField(
                        choices=[
                            ("completed", "Completed"),
                            ("pending", "Pending"),
                            ("failed", "Failed"),
                        ],
                        max_length=50,
                    ),
                ),
                ("created_at", models.DateTimeField(auto_now_add=True)),
                ("updated_at", models.DateTimeField(auto_now=True)),
                (
                    "ticket_id",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE, to="rentals.ticket"
                    ),
                ),
                (
                    "user_id",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
            ],
        ),
    ]
