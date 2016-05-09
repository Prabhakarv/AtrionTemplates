# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ProjectTemplate', '0002_auto_20160428_0628'),
    ]

    operations = [
        migrations.RenameField(
            model_name='employee',
            old_name='employee_contact',
            new_name='employee_contactNumber',
        ),
        migrations.AddField(
            model_name='projectdetails',
            name='project_status',
            field=models.TextField(default=b'Initial'),
            preserve_default=True,
        ),
    ]
