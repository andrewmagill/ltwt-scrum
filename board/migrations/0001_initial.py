# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Sprint',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False, auto_created=True, verbose_name='ID')),
                ('name', models.CharField(blank=True, default='', max_length=100)),
                ('description', models.TextField(blank=True, default='')),
                ('end', models.DateField(unique=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Tak',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False, auto_created=True, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('description', models.TextField(blank=True, default='')),
                ('status', models.SmallIntegerField(choices=[(1, 'Not Started'), (2, 'In Progress'), (3, 'Testing'), (4, 'Done')], default=1)),
                ('order', models.SmallIntegerField(default=0)),
                ('started', models.DateField(null=True, blank=True)),
                ('due', models.DateField(null=True, blank=True)),
                ('completed', models.DateField(null=True, blank=True)),
                ('assigned', models.ForeignKey(null=True, blank=True, to=settings.AUTH_USER_MODEL)),
                ('sprint', models.ForeignKey(null=True, blank=True, to='board.Sprint')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
