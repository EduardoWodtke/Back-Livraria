from django.db import models

from core.models import Autor, Categoria, Editora


class Livro(models.Model):
    titulo = models.CharField(max_length=255)
    isbn = models.CharField(max_length=255, blank=True, null=True)
    quantidade = models.IntegerField(default=0, blank=True, null=True)
    preco = models.DecimalField(max_digits=7, decimal_places=2, default=0, blank=True, null=True)
    categoria = models.ForeignKey(Categoria, on_delete=models.PROTECT, related_name="livros", null=False, blank=False)
    editora = models.ForeignKey(Editora, on_delete=models.PROTECT, related_name="livros")
    autor = models.ManyToManyField(Autor, related_name="livros")

    def __str__(self):
        return f"(id {self.id}) {self.titulo} R${self.preco} | informações adicionais: Categoria: {self.categoria}, Editora: {self.editora}, Autores:{self.autor} (Qnt:{self.quantidade})|"
