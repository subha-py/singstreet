# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        ('artist', '0002_auto_20160928_1509'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='artist',
            name='slug',
        ),
        migrations.AlterField(
            model_name='artist',
            name='country',
            field=models.CharField(default='india', max_length=255),
        ),
        migrations.AlterField(
            model_name='artist',
            name='listens',
            field=models.BigIntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='artist',
            name='location',
            field=models.CharField(default='kolkata', max_length=255),
        ),
        migrations.AlterField(
            model_name='artist',
            name='loved',
            field=models.BigIntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='artist',
            name='user',
            field=models.OneToOneField(to=settings.AUTH_USER_MODEL),
        ),
    ]
