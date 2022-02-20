from django.urls import path
from .views import (VacancyDetailView, VacancyListView, VacancyCreateView,
                         CreateEmployerView, VacancyDeleteView,VacancyUpdateView)


urlpatterns = [
    path('', VacancyListView.as_view(), name='vacancy_list'),

    path('<int:pk>/',
    VacancyDetailView.as_view(), name='vacancy_detail'),

    path('new/', VacancyCreateView.as_view(), name='vacancy_create'),
    path('new/emp', CreateEmployerView.as_view(), name='add_employer'),

    path('<int:pk>/update/',
    VacancyUpdateView.as_view(), name='vacancy_update'),

    path('<int:pk>/remove/',
    VacancyDeleteView.as_view(), name='vacancy_delete'),
]