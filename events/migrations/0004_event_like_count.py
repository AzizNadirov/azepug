# Generated by Django 4.0.1 on 2022-02-12 02:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('events', '0003_event_participants'),
    ]

    operations = [
        migrations.AddField(
            model_name='event',
            name='like_count',
            field=models.IntegerField(default=0),
        ),
    ]
