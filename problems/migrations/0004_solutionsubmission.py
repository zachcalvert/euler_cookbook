# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('problems', '0003_auto_20150618_1829'),
    ]

    operations = [
        migrations.CreateModel(
            name='SolutionSubmission',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('submitted', models.DateTimeField(auto_now_add=True)),
                ('solution', models.CharField(max_length=500)),
                ('submitted_by', models.CharField(max_length=30)),
                ('problem', models.ForeignKey(to='problems.Problem')),
            ],
        ),
    ]
