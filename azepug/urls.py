from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('blogs/', include('blog.urls')),
    path('', include('home.urls')),
    path('admin/', admin.site.urls),
]
