# Generated by Django 5.0.2 on 2024-08-23 17:10

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("core", "0019_remove_editora_pais_autor_email_editora_cidade_and_more"),
    ]

    operations = [
        migrations.RenameField(
            model_name="livro",
            old_name="autor",
            new_name="autores",
        ),
    ]
