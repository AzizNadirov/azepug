from django.urls import path

from .views import PostListView, PostDetailView, PostCreateView
app_name = 'blog'

urlpatterns = [
    path('', PostListView.as_view(), name='post_list'),

    path('post/<int:pk>/',
    PostDetailView.as_view(), name='about_post'),

    path('new/', PostCreateView.as_view(), name='create_post'),
]