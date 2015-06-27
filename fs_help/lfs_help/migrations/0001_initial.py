# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Language',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=30, verbose_name='name')),
                ('code', models.CharField(help_text='Two lowercase letters. Ex: no for Norwegian', max_length=2, verbose_name='code')),
            ],
            options={
                'ordering': ['name'],
                'verbose_name': 'language',
                'verbose_name_plural': 'languages',
            },
        ),
        migrations.CreateModel(
            name='Topic',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('title', models.CharField(max_length=100, verbose_name='title')),
                ('slug', models.CharField(help_text='www.filtersystem.no/no/[kode]', max_length=100, verbose_name='code')),
                ('content', models.TextField(verbose_name='content')),
                ('order', models.IntegerField(default=10, help_text='Sorting according to other documents with same superior', verbose_name='order')),
                ('need_auth', models.BooleanField(verbose_name='need authorisation')),
                ('active', models.BooleanField(verbose_name='active')),
                ('language', models.ForeignKey(verbose_name='languages', to='lfs_help.Language')),
                ('parent', models.ForeignKey(related_name='children', verbose_name='superior', blank=True, to='lfs_help.Topic', null=True)),
                ('saved_by', models.ForeignKey(to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'topic',
                'verbose_name_plural': 'topics',
            },
        ),
        migrations.CreateModel(
            name='UserGroup',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=30, verbose_name='name')),
                ('code', models.CharField(unique=True, max_length=3, verbose_name='code')),
            ],
            options={
                'ordering': ['code'],
                'verbose_name': 'user group',
                'verbose_name_plural': 'user groups',
            },
        ),
        migrations.AddField(
            model_name='topic',
            name='user_groups',
            field=models.ManyToManyField(help_text='Which user groups should have access to this document. If everyone should have access do not select anyone.\n', to='lfs_help.UserGroup', null=True, verbose_name='user groups', blank=True),
        ),
        migrations.AlterUniqueTogether(
            name='topic',
            unique_together=set([('language', 'slug')]),
        ),
    ]
