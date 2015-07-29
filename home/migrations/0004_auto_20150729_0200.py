# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0003_product_catagory'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='catagory',
            field=models.CharField(max_length=30, default='no_catagory'),
        ),
    ]
