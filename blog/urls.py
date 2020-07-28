from django.urls import path

from .views import PostListView, post_detail, PostCreateView, PostUpdateView, PostDeleteView
app_name = 'blog'

urlpatterns = [
    path('', PostListView.as_view(), name='post_list'),

    path('post/<int:pk>/',
    post_detail , name='about_post'),

    path('new/', PostCreateView.as_view(), name='create_post'),

    path('post/<int:pk>/update/',
    PostUpdateView.as_view(), name='update_post'),

    path('post/<int:pk>/remove/',
    PostDeleteView.as_view(), name='delete_post'),
]