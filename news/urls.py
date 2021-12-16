from django.urls import path

from .views import NewsListView, NewsDetailView, NewsCreateView, NewsUpdateView, NewsDeleteView


urlpatterns = [
    path('', NewsListView.as_view(), name='news_list'),

    path('<int:pk>/',
    NewsDetailView.as_view() , name='news_detail'),

    path('new/', NewsCreateView.as_view(), name='news_create'),

    path('<int:pk>/update/',
    NewsUpdateView.as_view(), name='news_update'),

    path('<int:pk>/remove/',
    NewsDeleteView.as_view(), name='news_delete'),
]