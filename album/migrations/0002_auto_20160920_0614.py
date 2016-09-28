# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('album', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='album',
            name='listens',
            field=models.BigIntegerField(default=0),
        ),
        migrations.AddField(
            model_name='album',
            name='loved',
            field=models.BigIntegerField(default=0),
        ),
    ]
