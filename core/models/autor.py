from django.db import models


class Autor(models.Model):
    nome = models.CharField(max_length=30)
    email = models.EmailField(blank=True, null=True)

    def __str__(self):
        return f"{self.nome.upper()} ({self.id})"

    class Meta:
        verbose_name_plural = "Autores"
