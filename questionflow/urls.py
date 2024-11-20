from django.urls import path
from . import views

app_name='questionflow'
urlpatterns = [
    path('', views.question_list, name='questions'),
    path('recent-questions/', views.recent_questions, name='recent_question'),
    path('<tag>/', views.question_list, name='tagger'),
    path('question-create/', views.question_create, name='question-create'),
    path('question-detail/<str:pk>/', views.question_detail, name='question-detail'),
    path('upvote-question/<str:pk>/', views.upvote_question, name='upvote_question')
]
