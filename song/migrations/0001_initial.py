# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import autoslug.fields
import song.models


class Migration(migrations.Migration):

    dependencies = [
        ('album', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Membership',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False, verbose_name='ID', auto_created=True)),
                ('date_joined', models.DateTimeField(auto_now_add=True)),
                ('album', models.ForeignKey(to='album.Album')),
            ],
        ),
        migrations.CreateModel(
            name='Song',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False, verbose_name='ID', auto_created=True)),
                ('name', models.CharField(max_length=500)),
                ('slug', autoslug.fields.AutoSlugField(unique=True, editable=False, populate_from='name')),
                ('genre', models.CharField(choices=[('blues', 'Blues'), ('comedy', 'Comedy'), ('country', 'Country'), ('easy', 'Easy Listening'), ('edm', 'EDM'), ('folk', 'Folk'), ('hiphop', 'Hip-Hop'), ('jazz', 'Jazz'), ('pop', 'Pop'), ('rnb', 'R&B and soul'), ('rock', 'Rock')], max_length=200, default='pop')),
                ('file', models.FileField(upload_to=song.models.song_directory_path, null=True)),
                ('listens', models.BigIntegerField(default=0)),
                ('loved', models.BigIntegerField(default=0)),
                ('content', models.TextField(blank=True)),
                ('lyrics', models.TextField(blank=True)),
                ('timestamp', models.DateTimeField(auto_now_add=True)),
                ('duration', models.IntegerField(default=0)),
                ('album', models.ManyToManyField(to='album.Album', through='song.Membership')),
            ],
            options={
                'ordering': ['-timestamp'],
            },
        ),
        migrations.AddField(
            model_name='membership',
            name='song',
            field=models.ForeignKey(to='song.Song'),
        ),
    ]
