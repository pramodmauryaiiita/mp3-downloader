# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import oauth2client.django_orm
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        ('User', '__first__'),
    ]

    operations = [
        migrations.CreateModel(
            name='CredentialsModel',
            fields=[
                ('id', models.ForeignKey(primary_key=True, serialize=False, to=settings.AUTH_USER_MODEL)),
                ('credential', oauth2client.django_orm.CredentialsField(null=True)),
            ],
        ),
        migrations.CreateModel(
            name='FlowModel',
            fields=[
                ('id', models.ForeignKey(primary_key=True, serialize=False, to=settings.AUTH_USER_MODEL)),
                ('flow', oauth2client.django_orm.FlowField(null=True)),
            ],
        ),
    ]
