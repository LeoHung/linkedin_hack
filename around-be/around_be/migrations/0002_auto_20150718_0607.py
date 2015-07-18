# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('around_be', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='message',
            name='unlock_type',
            field=models.IntegerField(null=True),
            preserve_default=True,
        ),
    ]
