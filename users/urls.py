from django.urls import path
from .views import register, TreasureListView



urlpatterns=[
    path('', register, name='register'),
    ]