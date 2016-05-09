# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ProjectTemplate', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='customer',
            name='cust_address',
            field=models.TextField(default=None, max_length=200),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='employee',
            name='employee_address',
            field=models.TextField(default=None, max_length=200),
            preserve_default=True,
        ),
    ]
