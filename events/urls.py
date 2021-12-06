from django.urls import path

from .views import EventCreateView, EventListView, EventUpdateView, EventDetailView, EventDeleteView

urlpatterns = [
    path('', EventListView.as_view(), name='event_list'),

    path('event/<int:pk>/',
    EventDetailView.as_view() , name='about_event'),

    path('new/', EventCreateView.as_view(), name='create_event'),

    path('event/<int:pk>/update/',
    EventUpdateView.as_view(), name='update_event'),

    path('event/<int:pk>/remove/',
    EventDeleteView.as_view(), name='delete_event'),
]