# Generated by Django 3.2.9 on 2021-12-16 11:38

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='comment',
            name='post',
        ),
        migrations.AddField(
            model_name='comment',
            name='news',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, related_name='n_comments', to='news.news'),
            preserve_default=False,
        ),
    ]
