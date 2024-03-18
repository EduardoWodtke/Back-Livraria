from django.db import models


class Categoria(models.Model):
    descricao = models.CharField(max_length=100, unique=True)

    def __str__(self):
        # return self.descricao.upper()
        return f"{self.descricao.upper()} ({self.id})"
