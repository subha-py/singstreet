# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import autoslug.fields


class Migration(migrations.Migration):

    dependencies = [
        ('album', '0003_auto_20160928_1509'),
    ]

    operations = [
        migrations.AlterField(
            model_name='album',
            name='slug',
            field=autoslug.fields.AutoSlugField(editable=False, populate_from='name', unique_with=('artist__user__username',)),
        ),
    ]
