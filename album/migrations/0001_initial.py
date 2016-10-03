# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import autoslug.fields
import album.models


class Migration(migrations.Migration):

    dependencies = [
        ('artist', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Album',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False, verbose_name='ID', auto_created=True)),
                ('name', models.CharField(max_length=255)),
                ('slug', autoslug.fields.AutoSlugField(unique=True, editable=False, populate_from='name')),
                ('content', models.TextField(blank=True)),
                ('image', models.ImageField(upload_to=album.models.album_directory_path, null=True)),
                ('loved', models.BigIntegerField(default=0)),
                ('listens', models.BigIntegerField(default=0)),
                ('timestamp', models.DateTimeField(auto_now_add=True)),
                ('duration', models.IntegerField(default=0)),
                ('artist', models.ForeignKey(to='artist.Artist')),
            ],
            options={
                'ordering': ['-timestamp'],
            },
        ),
        migrations.AlterUniqueTogether(
            name='album',
            unique_together=set([('name', 'artist')]),
        ),
    ]
