# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True, verbose_name='ID', auto_created=True)),
                ('product_id', models.CharField(max_length=30)),
                ('name', models.CharField(max_length=30)),
                ('author', models.CharField(max_length=100)),
                ('year', models.IntegerField()),
            ],
        ),
    ]
