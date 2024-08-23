from django.db import models


class Editora(models.Model):
    nome = models.CharField(max_length=100)
    email = models.EmailField(blank=True, null=True)
    cidade = models.CharField(max_length=100, blank=True, null=True)
    site = models.URLField(max_length=200, blank=True, null=True)

    def __str__(self):
        # return self.nome.upper()
        return f"{self.nome.upper()} ({self.id})"
