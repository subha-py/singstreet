# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import song.models
import autoslug.fields


class Migration(migrations.Migration):

    dependencies = [
        ('album', '0001_initial'),
        ('artist', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Song',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, serialize=False, auto_created=True)),
                ('title', models.CharField(max_length=500)),
                ('slug', autoslug.fields.AutoSlugField(editable=False, populate_from='title', unique_with=('artist__user__username',))),
                ('genre', models.CharField(default='pop', max_length=200, choices=[('blues', 'Blues'), ('comedy', 'Comedy'), ('country', 'Country'), ('easy', 'Easy Listening'), ('edm', 'EDM'), ('folk', 'Folk'), ('hiphop', 'Hip-Hop'), ('jazz', 'Jazz'), ('pop', 'Pop'), ('rnb', 'R&B and soul'), ('rock', 'Rock')])),
                ('file', models.FileField(upload_to=song.models.song_directory_path, null=True)),
                ('listens', models.BigIntegerField()),
                ('loved', models.BigIntegerField()),
                ('content', models.TextField()),
                ('lyrics', models.TextField()),
                ('timestamp', models.DateTimeField(auto_now_add=True)),
                ('duration', models.IntegerField(default=0)),
                ('album', models.ManyToManyField(to='album.Album')),
                ('artist', models.ForeignKey(to='artist.Artist')),
            ],
        ),
    ]
