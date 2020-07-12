from django.contrib import admin
from django.urls import path, include

from users import views as users_views

urlpatterns = [
    path('blogs/', include('blog.urls')),
    path('', include('home.urls')),
    path('admin/', admin.site.urls),
    path('register/', users_views.register,name='register'),
]
