    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('blogs/', include('blog.urls')),
    path('', include('home.urls')),
    path('admin/', admin.site.urls),
]
