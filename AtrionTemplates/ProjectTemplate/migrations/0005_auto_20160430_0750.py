# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ProjectTemplate', '0004_auto_20160428_0959'),
    ]

    operations = [
        migrations.AlterField(
            model_name='projectdetails',
            name='project_startdate',
            field=models.DateTimeField(default=None),
            preserve_default=True,
        ),
    ]
