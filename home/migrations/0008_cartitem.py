# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0007_product_url'),
    ]

    operations = [
        migrations.CreateModel(
            name='CartItem',
            fields=[
                ('id', models.AutoField(auto_created=True, verbose_name='ID', primary_key=True, serialize=False)),
                ('cart_id', models.CharField(max_length=50)),
                ('date_added', models.DateTimeField(auto_now_add=True)),
                ('quantity', models.IntegerField(default=1)),
                ('product', models.ForeignKey(to='home.Product')),
            ],
            options={
                'db_table': 'cart_items',
                'ordering': ['date_added'],
            },
        ),
    ]
