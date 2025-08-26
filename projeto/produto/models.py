from django.db import models

class Produto(models.Model):
    importado = models.BooleanField(default=False, verbose_name="Importado")
    created = models.DateTimeField(max_length=8, verbose_name="NCM")
    produto = models.CharField(max_length=100, unique=True, verbose_name="Produto")
    preco = models.DecimalField("Preço", max_digits=7, decimal_places=2)
    estoque = models.IntegerField("Estoque atual")
    estoque_minimo = models.PositiveBigIntegerField("Estoque mínimo", default=0)

    class Meta:
        ordering = ('produto',)
        verbose_name = "Produto"
        verbose_name_plural = "Produtos"

    def __str__(self):
        return str(self.produto)
