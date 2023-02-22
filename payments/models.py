from django.db import models


class Item(models.Model):
    name = models.CharField(verbose_name="Название", max_length=50)
    description = models.TextField(verbose_name="Описание", max_length=2000)
    price = models.IntegerField(verbose_name="Цена")

    class Meta:
        verbose_name = "Товар"
        verbose_name_plural = "Товары"

    def __str__(self):
        return self.name
