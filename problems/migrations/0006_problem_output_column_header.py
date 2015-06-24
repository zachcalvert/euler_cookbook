# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('problems', '0005_auto_20150619_2222'),
    ]

    operations = [
        migrations.AddField(
            model_name='problem',
            name='output_column_header',
            field=models.CharField(max_length=80, null=True, blank=True),
        ),
    ]
