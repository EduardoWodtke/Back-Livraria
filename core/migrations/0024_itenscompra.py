# Generated by Django 5.0.2 on 2024-09-13 16:58

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("core", "0023_compra"),
    ]

    operations = [
        migrations.CreateModel(
            name="ItensCompra",
            fields=[
                ("id", models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name="ID")),
                ("quantidade", models.IntegerField(default=1)),
                (
                    "compra",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE, related_name="itens", to="core.compra"
                    ),
                ),
                (
                    "livro",
                    models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name="+", to="core.livro"),
                ),
            ],
        ),
    ]
