# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('problems', '0002_problem_solution'),
    ]

    operations = [
        migrations.AlterField(
            model_name='problem',
            name='description',
            field=models.CharField(max_length=600),
        ),
    ]
