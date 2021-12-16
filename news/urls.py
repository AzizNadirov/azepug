from django.urls import path

from .views import NewsListView, NewsDetailView, NewsCreateView, NewsUpdateView, NewsDeleteView


urlpatterns = [
    path('', NewsListView.as_view(), name='list_news'),

    path('<int:pk>/',
    NewsDetailView.as_view() , name='news_detail'),

    path('new/', NewsCreateView.as_view(), name='create_news'),

    path('<int:pk>/update/',
    NewsUpdateView.as_view(), name='update_news'),

    path('<int:pk>/remove/',
    NewsDeleteView.as_view(), name='delete_news'),
]