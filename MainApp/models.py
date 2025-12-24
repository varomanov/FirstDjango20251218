from django.db import models


class Item(models.Model):
    name = models.CharField(max_length=100)
    brand = models.CharField(max_length=100)
    count = models.PositiveIntegerField()
    description = models.TextField(max_length=300, default='Описание элемента')

    def __repr__(self):
        return f"Item(id:{self.pk}, name:{self.name})"
