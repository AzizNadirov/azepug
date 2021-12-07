from django.urls import path

from .views import QuestionListView, QuestionDetailView, QuestionDeleteView, QuestionCreateView

urlpatterns = [
    path('', QuestionListView.as_view(), name = 'question_list'),
    path('create/', QuestionCreateView.as_view(), name = 'question_create'),
    path('<int:id>/', QuestionDetailView.as_view(), name = 'question_detail'),
    path('del/<int:id>/', QuestionDeleteView.as_view(), name = 'question_delete'),

]