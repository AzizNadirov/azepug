# Generated by Django 4.0.1 on 2022-02-15 07:26

import ckeditor.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('forum', '0002_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='answer',
            name='content',
            field=ckeditor.fields.RichTextField(),
        ),
        migrations.AlterField(
            model_name='question',
            name='content',
            field=ckeditor.fields.RichTextField(),
        ),
    ]