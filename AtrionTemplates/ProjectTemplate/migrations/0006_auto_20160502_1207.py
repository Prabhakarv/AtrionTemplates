# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ProjectTemplate', '0005_auto_20160430_0750'),
    ]

    operations = [
        migrations.AlterField(
            model_name='projectdetails',
            name='project_startdate',
            field=models.DateField(default=None),
            preserve_default=True,
        ),
    ]
