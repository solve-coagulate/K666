# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.AutoField(serialize=False, verbose_name='ID', auto_created=True, primary_key=True)),
                ('text', models.TextField()),
                ('created_on', models.DateTimeField(auto_now_add=True)),
                (
                    'created_by',
                    models.ForeignKey(
                        to=settings.AUTH_USER_MODEL,
                        on_delete=models.CASCADE,
                    ),
                ),
                (
                    'parent',
                    models.ForeignKey(
                        null=True,
                        to='comments.Comment',
                        on_delete=models.CASCADE,
                    ),
                ),
            ],
            options={
                'ordering': ['-id'],
            },
        ),
    ]
