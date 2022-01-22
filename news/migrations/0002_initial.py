# Generated by Django 4.0.1 on 2022-01-22 00:57

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import taggit.managers


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('news', '0001_initial'),
        ('taggit', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.AddField(
            model_name='news',
            name='author',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='news', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='news',
            name='likes',
            field=models.ManyToManyField(related_name='liked_news', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='news',
            name='tags',
            field=taggit.managers.TaggableManager(help_text='A comma-separated list of tags.', through='taggit.TaggedItem', to='taggit.Tag', verbose_name='Tags'),
        ),
        migrations.AddField(
            model_name='comment',
            name='author',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='n_comments', to=settings.AUTH_USER_MODEL, verbose_name='müəllif'),
        ),
        migrations.AddField(
            model_name='comment',
            name='news',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='n_comments', to='news.news'),
        ),
    ]
