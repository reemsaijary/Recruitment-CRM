from django.urls import path
from . import views

urlpatterns = [
    path('', views.dashboard, name='dashboard'),

    path('candidates/', views.candidates_list, name='candidates_list'),
    path('candidates/add/', views.add_candidate, name='add_candidate'),
    path('candidates/<int:candidate_id>/', views.candidate_details, name='candidate_details'),
    path('candidates/<int:candidate_id>/edit/', views.edit_candidate, name='edit_candidate'),
    path('candidates/<int:candidate_id>/delete/', views.delete_candidate, name='delete_candidate'),

    path('companies/', views.companies_list, name='companies_list'),
    path('companies/add/', views.add_company, name='add_company'),
    path('companies/<int:company_id>/', views.company_details, name='company_details'),
    path('companies/<int:company_id>/edit/', views.edit_company, name='edit_company'),
    path('companies/<int:company_id>/delete/', views.delete_company, name='delete_company'),

    path('jobs/', views.jobs_list, name='jobs_list'),
    path('jobs/add/', views.add_job, name='add_job'),
    path('jobs/<int:job_id>/', views.job_details, name='job_details'),
    path('jobs/<int:job_id>/edit/', views.edit_job, name='edit_job'),
    path('jobs/<int:job_id>/delete/', views.delete_job, name='delete_job'),








]
