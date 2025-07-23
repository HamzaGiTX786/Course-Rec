from django.urls import path
from . import views

urlpatterns = [
    path('', views.all_users),
    path('create/', views.create_user),
    path('login/', views.login),
    path('refresh/', views.refresh),
    path('logout/', views.logout),
    path('conversation/', views.get_conversations),
    path('all-conversations/', views.all_conversations),
    path('rename-conversation/', views.rename_conversation),
    path('forgot-password/', views.forgot_password),
    path('delete-conversation/', views.delete_convservation)
]