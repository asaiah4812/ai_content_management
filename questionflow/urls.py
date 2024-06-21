from django.urls import path
from . import views

app_name='questionflow'
urlpatterns = [
    path('', views.question_list, name='questions'),
    path('<tag>/', views.question_list, name='tagger'),
    path('question-create/', views.question_create, name='question-create'),
    path('question-detail/<str:pk>/', views.question_detail, name='question-detail')
]
