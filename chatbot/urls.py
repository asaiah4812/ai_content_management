from django.urls import path
from . import views

# app_name = 'chat'

urlpatterns = [
    path("", views.chat, name="chatbot"),
    path("ask_question/", views.ask_question, name="ask_question"),
]
