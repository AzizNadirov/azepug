from django.urls import path
from .views import blog_list, about_post
app_name = 'blog'

urlpatterns = [
    path('', blog_list),
    path('<int:year>/<int:month>/<int:day>/<slug:post>/',
    about_post, name = 'about_post')
]