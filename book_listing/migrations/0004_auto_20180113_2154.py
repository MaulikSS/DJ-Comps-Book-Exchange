# -*- coding: utf-8 -*-
# Generated by Django 1.11.8 on 2018-01-13 16:24
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('book_listing', '0003_auto_20180113_0010'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='BookList',
            new_name='Book_List',
        ),
    ]
