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

    path('applications/', views.applications_list, name='applications_list'),
    path('applications/add/', views.add_application, name='add_application'),
    path('applications/<int:application_id>/', views.application_details, name='application_details'),
    path('applications/<int:application_id>/edit/', views.edit_application, name='edit_application'),
    path('applications/<int:application_id>/delete/', views.delete_application, name='delete_application'),

    path('interviews/', views.interviews_list, name='interviews_list'),
    path('interviews/add/', views.add_interview, name='add_interview'),
    path('interviews/<int:interview_id>/', views.interview_details, name='interview_details'),
    path('interviews/<int:interview_id>/edit/', views.edit_interview, name='edit_interview'),
    path('interviews/<int:interview_id>/delete/', views.delete_interview, name='delete_interview'),

    path('evaluations/', views.evaluations_list, name='evaluations_list'),
    path('evaluations/add/', views.add_evaluation, name='add_evaluation'),
    path('evaluations/<int:evaluation_id>/', views.evaluation_details, name='evaluation_details'),
    path('evaluations/<int:evaluation_id>/edit/', views.edit_evaluation, name='edit_evaluation'),
    path('evaluations/<int:evaluation_id>/delete/', views.delete_evaluation, name='delete_evaluation'),

    path('activities/', views.activities_list, name='activities_list'),
    path('activities/add/', views.add_activity, name='add_activity'),
    path('activities/<int:activity_id>/', views.activity_details, name='activity_details'),
    path('activities/<int:activity_id>/edit/', views.edit_activity, name='edit_activity'),
    path('activities/<int:activity_id>/delete/', views.delete_activity, name='delete_activity'),


]
