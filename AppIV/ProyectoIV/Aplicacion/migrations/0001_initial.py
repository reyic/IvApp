# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Calification',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('player', models.CharField(max_length=100)),
                ('calification', models.IntegerField(default=0)),
            ],
        ),
        migrations.CreateModel(
            name='Enterprise',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=100)),
                ('town', models.CharField(max_length=50)),
                ('sector', models.CharField(max_length=100)),
            ],
        ),
        migrations.AddField(
            model_name='calification',
            name='enterprise',
            field=models.ForeignKey(to='Aplicacion.Enterprise'),
        ),
    ]
