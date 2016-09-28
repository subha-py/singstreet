# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import album.models


class Migration(migrations.Migration):

    dependencies = [
        ('album', '0002_auto_20160920_0614'),
    ]

    operations = [
        migrations.AlterField(
            model_name='album',
            name='image',
            field=models.ImageField(null=True, upload_to=album.models.album_directory_path),
        ),
    ]
