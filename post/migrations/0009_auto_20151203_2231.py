# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('post', '0008_auto_20151203_2141'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='picture',
            field=models.ImageField(null=True, upload_to=b''),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='post',
            name='url_picture',
            field=models.CharField(max_length=200, null=True),
            preserve_default=True,
        ),
    ]
