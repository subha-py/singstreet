# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import artist.models


class Migration(migrations.Migration):

    dependencies = [
        ('artist', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='artist',
            name='image',
            field=models.ImageField(null=True, upload_to=artist.models.artist_directory_path),
        ),
    ]
