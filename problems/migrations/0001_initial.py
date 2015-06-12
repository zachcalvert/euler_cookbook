# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Problem',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('number', models.IntegerField(default=1)),
                ('title', models.CharField(max_length=60)),
                ('description', models.CharField(max_length=500)),
                ('link', models.URLField(help_text=b'URL on Project Euler')),
                ('solved', models.BooleanField(default=False)),
            ],
        ),
    ]
