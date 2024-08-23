# Generated by Django 5.0.2 on 2024-08-23 16:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("core", "0017_livro_capa"),
    ]

    operations = [
        migrations.AddField(
            model_name="editora",
            name="email",
            field=models.EmailField(default=1, max_length=254),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name="editora",
            name="pais",
            field=models.CharField(default=1, max_length=100),
            preserve_default=False,
        ),
    ]
