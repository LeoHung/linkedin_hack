# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('around_be', '0003_auto_20150718_0635'),
    ]

    operations = [
        migrations.AddField(
            model_name='message',
            name='lock',
            field=models.BooleanField(default=False),
        ),
    ]
