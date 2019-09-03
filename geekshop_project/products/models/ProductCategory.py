from django.db import models

class ProductCategory(models.Model):
    name = models.CharField(verbose_name='имя продукта', max_length=128, unique=True)
    description = models.TextField(verbose_name='описание продукта', blank=True)

    modified = models.DateTimeField(
        auto_now=True
    )
    created = models.DateTimeField(
        auto_now_add=True
    )

    def __str__(self):
        return f"{self.name}"
