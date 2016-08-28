# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2016-08-28 02:42
from __future__ import unicode_literals

from decimal import Decimal
from django.db import migrations
import djmoney.models.fields


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='orderitem',
            name='price',
            field=djmoney.models.fields.MoneyField(decimal_places=2, default=Decimal('0.0'), default_currency='USD', max_digits=8),
        ),
    ]