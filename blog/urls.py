from django.urls import path

from .views import (PostListView, PostDetailView, PostCreateView,
     PostUpdateView, PostDeleteView, PostLikeView, PostSaveView)


urlpatterns = [
    path('', PostListView.as_view(), name='blog_list'),

    path('<int:pk>/',
    PostDetailView.as_view() , name='blog_detail'),

    path('new/', PostCreateView.as_view(), name='blog_create'),
    path('<int:pk>/like/', PostLikeView.as_view(), name='blog_like'),
    path('<int:pk>/save/', PostSaveView.as_view(), name='blog_save'),

    path('<int:pk>/update/',
    PostUpdateView.as_view(), name='blog_update'),

    path('<int:pk>/remove/',
    PostDeleteView.as_view(), name='blog_delete'),
]