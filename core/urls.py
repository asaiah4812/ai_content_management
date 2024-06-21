from django.urls import path

from . import views


urlpatterns = [
    path("", views.home, name="home"),
    path('dashboard/', views.dashboard, name="dashboard"),
    path('task_list/', views.todo_list, name="todo_list"),
    path('submit-task/', views.submit_task, name="submit-task"),
    path('complete-task/<str:pk>/', views.complete_task, name="complete-task"),
    path('delete-task/<str:pk>/', views.delete_task, name="delete-task"),
    path('profile/<username>/', views.profile, name="profile_detail"),
    path('profile/', views.profile, name="profile"),
    path('profile_edit/', views.profile_edit_view, name="profile_edit"),
    # path('follow/<int:user_id>/', views.follow_user, name='follow_user'),
    # path('unfollow/<int:user_id>/', views.unfollow_user, name='unfollow_user'),
]