from django.contrib import admin
from django.db.models.base import Model
from .models import News

admin.site.register(News)