# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import artist.models
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Artist',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, serialize=False, auto_created=True)),
                ('image', models.ImageField(upload_to=artist.models.artist_directory_path, null=True)),
                ('country', models.CharField(default='india', max_length=255)),
                ('location', models.CharField(default='kolkata', max_length=255)),
                ('listens', models.BigIntegerField(default=0)),
                ('loved', models.BigIntegerField(default=0)),
                ('timestamp', models.DateTimeField(auto_now_add=True)),
                ('user', models.OneToOneField(to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
