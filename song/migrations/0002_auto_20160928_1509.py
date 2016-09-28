# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import song.models


class Migration(migrations.Migration):

    dependencies = [
        ('song', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='song',
            name='file',
            field=models.FileField(null=True, upload_to=song.models.song_directory_path),
        ),
        migrations.AlterField(
            model_name='song',
            name='genre',
            field=models.CharField(max_length=200, default='pop', choices=[('blues', 'Blues'), ('comedy', 'Comedy'), ('country', 'Country'), ('easy', 'Easy Listening'), ('edm', 'EDM'), ('folk', 'Folk'), ('hiphop', 'Hip-Hop'), ('jazz', 'Jazz'), ('pop', 'Pop'), ('rnb', 'R&B and soul'), ('rock', 'Rock')]),
        ),
    ]
