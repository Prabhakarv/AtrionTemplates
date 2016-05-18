# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ProjectTemplate', '0007_auto_20160512_1138'),
    ]

    operations = [
        migrations.AlterField(
            model_name='projectdetails',
            name='project_status',
            field=models.CharField(default=b'Initial', max_length=10),
            preserve_default=True,
        ),
    ]
