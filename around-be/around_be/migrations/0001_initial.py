# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Message',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('msg_type', models.CharField(max_length=20)),
                ('title', models.CharField(max_length=30)),
                ('doc', models.CharField(default=b'no description', max_length=200, null=True)),
                ('url', models.CharField(default=b'http://www.linkedin.com', max_length=100, null=True)),
                ('img_url', models.CharField(default=b'http://www.linkedin.com', max_length=100, null=True)),
                ('start_time', models.DateTimeField(null=True)),
                ('end_time', models.DateTimeField(null=True)),
                ('category', models.CharField(max_length=20)),
                ('unlock_type', models.IntegerField()),
                ('lat', models.DecimalField(null=True, max_digits=15, decimal_places=10)),
                ('lng', models.DecimalField(null=True, max_digits=15, decimal_places=10)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
