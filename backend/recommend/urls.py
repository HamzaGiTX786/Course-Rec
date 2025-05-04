from django.urls import path
from . import views

urlpatterns = [
    path('hello/', views.test),
    path('prompt/', views.recommend_courses)
]