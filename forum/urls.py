from django.urls import path

from .views import (QuestionListView, QuestionDetailView, QuestionDeleteView,
                        QuestionCreateView, QuestionUpdateView)

urlpatterns = [
    path('', QuestionListView.as_view(), name = 'question_list'),
    path('create/', QuestionCreateView.as_view(), name = 'question_create'),
     path('<int:pk>/update/', QuestionUpdateView.as_view(), name = 'question_update'),
    path('<int:pk>/', QuestionDetailView.as_view(), name = 'question_detail'),
    path('del/<int:pk>/', QuestionDeleteView.as_view(), name = 'question_delete'),

]