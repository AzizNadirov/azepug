from django.urls import path

from .views import PostListView, PostDetailView, PostCreateView, PostUpdateView, PostDeleteView


urlpatterns = [
    path('list/', PostListView.as_view(), name='post_list'),

    path('<int:pk>/',
    PostDetailView.as_view() , name='about_post'),

    path('new/', PostCreateView.as_view(), name='create_post'),

    path('<int:pk>/update/',
    PostUpdateView.as_view(), name='update_post'),

    path('<int:pk>/remove/',
    PostDeleteView.as_view(), name='delete_post'),
]