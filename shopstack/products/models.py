from django.db import models

import moneyed
from djmoney.models.fields import MoneyField

from stores.models import Store


class Product(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(max_length=500)
    price = MoneyField(
        max_digits=8,
        decimal_places=2,
        default_currency='USD'
    )
    released = models.DateTimeField(auto_now_add=True, auto_now=False)
    updated = models.DateTimeField(auto_now_add=False, auto_now=True)
    quantity = models.PositiveIntegerField()
    store = models.ForeignKey(
        Store,
        on_delete=models.CASCADE,
        related_name='products'
    )

    def __str__(self):
        return self.name
