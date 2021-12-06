from django.urls import path
from .views import (VacancyDetailView, VacancyListView, VacancyCreateView,
                    VacancyDeleteView,VacancyUpdateView
)


urlpatterns = [
    path('', VacancyListView.as_view(), name='vacancy_list'),

    path('vacancy/<int:pk>/',
    VacancyDetailView.as_view(), name='about_vacancy'),

    path('new/', VacancyCreateView.as_view(), name='create_vacancy'),

    path('post/<int:pk>/update/',
    VacancyUpdateView.as_view(), name='update_vacancy'),

    path('post/<int:pk>/remove/',
    VacancyDeleteView.as_view(), name='delete_vacancy'),
]