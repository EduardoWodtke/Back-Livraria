# Generated by Django 4.2.16 on 2024-09-27 17:59

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("core", "0025_alter_user_managers_user_passage_id"),
    ]

    operations = [
        migrations.AlterModelOptions(
            name="user",
            options={"verbose_name": "Usuário", "verbose_name_plural": "Usuários"},
        ),
    ]
