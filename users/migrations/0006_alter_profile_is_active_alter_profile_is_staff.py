# Generated by Django 4.0.1 on 2022-02-20 05:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0005_remove_profile_treasure_treasure_profile_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='is_active',
            field=models.BooleanField(default=True),
        ),
        migrations.AlterField(
            model_name='profile',
            name='is_staff',
            field=models.BooleanField(default=True),
        ),
    ]
