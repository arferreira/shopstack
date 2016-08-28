import uuid

from django.db import models

import moneyed
from djmoney.models.fields import MoneyField

from products.models import Product
from users.models import User, Address, PaymentMethod


class Order(models.Model):
    PENDING = 'PD'
    SHIPPED = 'SH'
    ARRIVED = 'AR'
    CANCELLED = 'CN'
    STATUS_CHOICES = (
        (PENDING, 'Pending'),
        (SHIPPED, 'Shipped'),
        (ARRIVED, 'Arrived'),
        (CANCELLED, 'Cancelled'),
    )
    buyer = models.ForeignKey(
        User,
        on_delete=models.SET_NULL,
        related_name='orders',
        null=True
    )
    ordnum = models.UUIDField(default=uuid.uuid4, unique=True, editable=False)
    placed = models.DateTimeField(auto_now_add=True, auto_now=False)
    updated = models.DateTimeField(auto_now_add=False, auto_now=False)
    shipping_address = models.ForeignKey(
        Address,
        related_name='shipping_add'
    )
    billing_address = models.ForeignKey(
        Address,
        related_name='billing_add'
    )
    payment_method = models.ForeignKey(
        PaymentMethod,
        related_name='payment_method'
    )
    products = models.ManyToManyField(
        Product,
        through='OrderItem'
    )
    status = models.CharField(
        max_length=2,
        choices=STATUS_CHOICES,
        default=PENDING
    )

    def __str__(self):
        return '{}'.format(str(self.ordnum)[:5])


class OrderItem(models.Model):
    order = models.ForeignKey(Order)
    product = models.ForeignKey(Product)
    # Must be a copy of product price at time of order
    price = MoneyField(
        max_digits=8,
        decimal_places=2,
        default_currency='USD'
    )
    notes = models.TextField(max_length=500, blank=True)

    def __str__(self):
        return '{0}-{1}'.format(str(self.order.ordnum), self.product.name)
