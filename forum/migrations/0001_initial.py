# Generated by Django 3.2.9 on 2021-12-07 12:04

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('blog', '0003_alter_post_author'),
    ]

    operations = [
        migrations.CreateModel(
            name='Answer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('body', models.TextField(verbose_name='Məzmun')),
                ('supports', models.IntegerField(default=0)),
                ('date_created', models.DateTimeField(auto_now_add=True)),
                ('last_edited', models.DateTimeField(default=models.DateTimeField(auto_now_add=True))),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='answers', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Question',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=128, verbose_name='Başlıq')),
                ('body', models.TextField(verbose_name='Məzmun')),
                ('supports', models.IntegerField(default=0)),
                ('date_created', models.DateTimeField(auto_now_add=True)),
                ('last_edited', models.DateTimeField(default=models.DateTimeField(auto_now_add=True))),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='questions', to=settings.AUTH_USER_MODEL)),
                ('tags', models.ManyToManyField(related_name='questions', to='blog.Tag')),
            ],
        ),
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('body', models.TextField(max_length=1024, verbose_name='Şərh')),
                ('created', models.DateTimeField(auto_now_add=True, verbose_name='Yaradılma tarixi')),
                ('updated', models.DateTimeField(auto_now=True, verbose_name='Yenilənmə tariix')),
                ('active', models.BooleanField(default=True, verbose_name='Aktiv')),
                ('image', models.ImageField(blank=True, null=True, upload_to='')),
                ('answer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='comments', to='forum.answer')),
                ('author', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='f_comments', to=settings.AUTH_USER_MODEL, verbose_name='müəllif')),
            ],
            options={
                'ordering': ('-created',),
            },
        ),
        migrations.AddField(
            model_name='answer',
            name='question',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='answers', to='forum.question'),
        ),
    ]
