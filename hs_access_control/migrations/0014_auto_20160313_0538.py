# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
from django.conf import settings
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('auth', '0006_require_contenttypes_0002'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('hs_access_control', '0013_auto_add_uniqueness_constraints'),
    ]

    operations = [
        migrations.CreateModel(
            name='GroupMembershipRequest',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('date_requested', models.DateTimeField(auto_now_add=True)),
                ('group_to_join', models.ForeignKey(related_name='g2gmrequest', to='auth.Group')),
                ('invitation_to', models.ForeignKey(related_name='iu2gmrequest', blank=True, to=settings.AUTH_USER_MODEL, null=True)),
                ('request_from', models.ForeignKey(related_name='ru2gmrequest', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.AddField(
            model_name='groupaccess',
            name='date_created',
            field=models.DateTimeField(default=datetime.datetime(2016, 3, 13, 5, 38, 42, 990769), auto_now_add=True),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='groupaccess',
            name='description',
            field=models.TextField(default=''),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='groupaccess',
            name='purpose',
            field=models.TextField(null=True, blank=True),
        ),
    ]
