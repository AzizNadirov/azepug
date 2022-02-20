from django.urls import path

from .views import EventCreateView, EventListView, EventUpdateView, EventDetailView, EventDeleteView

urlpatterns = [
    path('', EventListView.as_view(), name='event_list'),

    path('<int:pk>/',
    EventDetailView.as_view() , name='event_detail'),

    path('new/', EventCreateView.as_view(), name='event_create'),

    path('<int:pk>/update/',
    EventUpdateView.as_view(), name='event_update'),

    path('<int:pk>/remove/',
    EventDeleteView.as_view(), name='event_delete'),
]