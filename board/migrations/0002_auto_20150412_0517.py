# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('board', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Task',
            fields=[
                ('id', models.AutoField(verbose_name='ID', auto_created=True, serialize=False, primary_key=True)),
                ('name', models.CharField(max_length=100)),
                ('description', models.TextField(blank=True, default='')),
                ('status', models.SmallIntegerField(choices=[(1, 'Not Started'), (2, 'In Progress'), (3, 'Testing'), (4, 'Done')], default=1)),
                ('order', models.SmallIntegerField(default=0)),
                ('started', models.DateField(blank=True, null=True)),
                ('due', models.DateField(blank=True, null=True)),
                ('completed', models.DateField(blank=True, null=True)),
                ('assigned', models.ForeignKey(blank=True, null=True, to=settings.AUTH_USER_MODEL)),
                ('sprint', models.ForeignKey(blank=True, null=True, to='board.Sprint')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.RemoveField(
            model_name='tak',
            name='assigned',
        ),
        migrations.RemoveField(
            model_name='tak',
            name='sprint',
        ),
        migrations.DeleteModel(
            name='Tak',
        ),
    ]
