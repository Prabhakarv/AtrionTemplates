# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ProjectTemplate', '0006_auto_20160502_1207'),
    ]

    operations = [
        migrations.AlterField(
            model_name='projectdetails',
            name='project_status',
            field=models.TextField(default=b'Initial', max_length=50),
            preserve_default=True,
        ),
    ]
