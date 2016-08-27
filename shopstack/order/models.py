import uuid

from django.db import models

from products.models import Product
from user.models import User, Address, PaymentMethod


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
    ordnum = models.UUID(default=uuid.uuid4, unique=True, editable=False)
    placed = models.DateTimeField(auto_now_add=True, auto_now=False)
    updated = models.DateTimeField(auto_now_add=False, auto_now=False)
    shipping_address = models.ForeignKey(
        Address,
        related_name='shipping_address'
    )
    billing_address = models.ForeignKey(
        Address,
        related_name='billing_address'
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

    def __unicode__(self):
        return self.ordnum


class OrderItem(models.Model):
    order = models.ForeignKey(Order)
    product = models.ForeignKey(Product)
    # Must be a copy of product price at time of order
    price = models.MoneyField(
        max_digits=4,
        decimal_places=2,
        default_currency='USD'
    )
    notes = models.TextField(max_length=500)

    def save(self, *args, **kwargs):
        self.price = self.product.price
        super(OrderItem, self).save(*args, **kwargs)
