# Generated by Django 4.0.1 on 2022-02-15 07:26

import ckeditor.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('events', '0004_event_like_count'),
    ]

    operations = [
        migrations.AlterField(
            model_name='event',
            name='content',
            field=ckeditor.fields.RichTextField(),
        ),
    ]
