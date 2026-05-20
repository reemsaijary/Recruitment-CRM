from django.urls import path
from . import views

urlpatterns = [
    path('', views.dashboard, name='dashboard'),
    path('candidates/', views.candidates_list, name='candidates_list'),
]