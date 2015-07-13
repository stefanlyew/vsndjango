# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Vehicle',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('serial_number_pattern', models.CharField(max_length=12)),
                ('vehicle_trim_id', models.IntegerField()),
                ('year', models.IntegerField()),
                ('make', models.CharField(max_length=140)),
                ('model', models.CharField(max_length=140)),
                ('trim_name', models.CharField(max_length=300)),
                ('regexp', models.CharField(max_length=100)),
                ('wildcard_count', models.IntegerField()),
            ],
        ),
    ]
