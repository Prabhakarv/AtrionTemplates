# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ProjectTemplate', '0003_auto_20160428_0950'),
    ]

    operations = [
        migrations.RenameField(
            model_name='customer',
            old_name='cust_contact',
            new_name='cust_contact_number',
        ),
        migrations.RenameField(
            model_name='employee',
            old_name='employee_contactNumber',
            new_name='employee_contact_number',
        ),
    ]
