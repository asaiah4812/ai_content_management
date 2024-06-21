from django.urls import path
from . import views

app_name='content'

urlpatterns = [
    path('', views.contents, name='contents'),
    path('content_detail/<str:pk>/', views.content_detail, name='content-detail'),
]
