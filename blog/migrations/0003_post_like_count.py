# Generated by Django 4.0.1 on 2022-02-12 02:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='like_count',
            field=models.IntegerField(default=0),
        ),
    ]
