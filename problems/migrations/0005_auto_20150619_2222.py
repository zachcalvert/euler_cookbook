# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('problems', '0004_solutionsubmission'),
    ]

    operations = [
        migrations.CreateModel(
            name='Contribution',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('submitted', models.DateTimeField(auto_now_add=True)),
                ('solution', models.CharField(max_length=500)),
                ('submitted_by', models.CharField(max_length=30)),
                ('problem', models.ForeignKey(to='problems.Problem')),
            ],
        ),
        migrations.RemoveField(
            model_name='solutionsubmission',
            name='problem',
        ),
        migrations.DeleteModel(
            name='SolutionSubmission',
        ),
    ]
