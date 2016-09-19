# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('album', '0001_initial'),
        ('artist', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Song',
            fields=[
                ('id', models.AutoField(auto_created=True, verbose_name='ID', primary_key=True, serialize=False)),
                ('title', models.CharField(max_length=500)),
                ('slug', models.SlugField(max_length=500)),
                ('genre', models.CharField(max_length=10, choices=[('blues', 'Blues'), ('comedy', 'Comedy'), ('country', 'Country'), ('easy', 'Easy Listening'), ('edm', 'EDM'), ('folk', 'Folk'), ('hiphop', 'Hip-Hop'), ('jazz', 'Jazz'), ('pop', 'Pop'), ('rnb', 'R&B and soul'), ('rock', 'Rock')], default='pop')),
                ('listens', models.BigIntegerField()),
                ('loved', models.BigIntegerField()),
                ('content', models.TextField()),
                ('lyrics', models.TextField()),
                ('timestamp', models.DateTimeField(auto_now_add=True)),
                ('duration', models.DurationField()),
                ('album', models.ManyToManyField(to='album.Album')),
                ('artist', models.ForeignKey(to='artist.Artist')),
            ],
        ),
    ]
