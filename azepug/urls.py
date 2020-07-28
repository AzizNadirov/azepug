from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth import views as auth_views

from users import views as users_views

urlpatterns = [
    path('blogs/', include('blog.urls')),
    path('', include('home.urls')),
    path('admin/', admin.site.urls),
    path('register/', include('users.urls')),
    path('login/',auth_views.LoginView.as_view(template_name = 'users/login.html'), name = "login"),
    path('logout/',auth_views.LogoutView.as_view(template_name = 'users/logout.html'), name = "logout"),
    path('profile/', users_views.profile, name = 'profile'),
    path('edit/', users_views.edit_profile_view, name = 'edit_profile'),
    path('vacancies/', include('vacancy.urls'), name = 'vacancy'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)