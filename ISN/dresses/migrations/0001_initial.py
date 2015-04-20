# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Vetement',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('nom', models.CharField(max_length=200)),
                ('temp_max', models.IntegerField()),
                ('temp_min', models.IntegerField()),
                ('pluie', models.BooleanField()),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
