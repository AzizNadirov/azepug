# Generated by Django 3.2.9 on 2021-12-16 14:56

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('vacancy', '0003_vacancy_tags'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='comment',
            options={'ordering': ('-created_at',)},
        ),
        migrations.RenameField(
            model_name='comment',
            old_name='created',
            new_name='created_at',
        ),
    ]
