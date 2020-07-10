from django.urls import path
from .views import blog_list, about_post, create_post,update_post
from .views import BlogList_v
app_name = 'blog'

urlpatterns = [
    # path('', blog_list, name = 'blog_list'),
    path('', BlogList_v.as_view(), name = 'blog_list'),

    path('<int:year>/<int:month>/<int:day>/<slug:post>/',
    about_post, name = 'about_post'),

    path('create_post/', create_post, name='create_post'), 
    path('update_post/<int:pk>/', update_post, name='update_post'),
]