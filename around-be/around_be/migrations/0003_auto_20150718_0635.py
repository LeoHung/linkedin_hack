# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('around_be', '0002_auto_20150718_0607'),
    ]

    operations = [
        migrations.AlterField(
            model_name='message',
            name='unlock_type',
            field=models.CharField(max_length=20, null=True),
        ),
    ]
