# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('courses', '0002_auto_20141028_0439'),
    ]

    operations = [
        migrations.AddField(
            model_name='course',
            name='image',
            field=models.CharField(default='', max_length=200),
            preserve_default=False,
        ),
    ]
