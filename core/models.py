from django.db import models

class Categoria(models.Model):
    nome = models.CharField('Categoria', max_length=50)

    class Meta:
        verbose_name = 'Categoria'
        verbose_name_plural = 'Categorias'

    def set_default_categoria(self):
        return Categoria.objects.get_or_create(nome='Comida')[0]

    def __str__(self):
        return self.nome

class Tipo(models.Model):
    tipo = models.CharField('Tipo', max_length=50)

    class Meta:
        verbose_name = 'Tipo'
        verbose_name_plural = 'Tipos'

    def set_default_tipo(self):
        return Tipo.objects.get_or_create(tipo='Unidade')

    def __str__(self):
        return self.tipo

class Produto(models.Model):
    nome = models.CharField('Nome', max_length=100)
    categoria = models.ForeignKey(Categoria, on_delete=models.SET(Categoria.set_default_categoria))
    tipo = models.ForeignKey(Tipo, on_delete=models.SET(Tipo.set_default_tipo))
    preco = models.DecimalField('Preço', max_digits=5, decimal_places=2, default=0)
    ativo = models.BooleanField('Ativo?', default=True)

    class Meta:
        verbose_name = 'Produto'
        verbose_name_plural = 'Produtos'

    def __str__(self):
        return self.nome

