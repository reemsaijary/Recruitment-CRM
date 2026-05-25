from django.urls import path

from .views.auth_views import login_view, logout_view
from .views.company_views.dashboard_views import company_dashboard
from .views.candidate_views.dashboard_views import candidate_dashboard

from .views.admin_views.dashboard_views import dashboard
from .views.admin_views.candidate_views import *
from .views.admin_views.company_views import *
from .views.admin_views.job_views import *
from .views.admin_views.application_views import *
from .views.admin_views.interview_views import *
from .views.admin_views.evaluation_views import *
from .views.admin_views.activity_views import *

from .views.company_views.job_views import *
from .views.company_views.application_views import *
from .views.candidate_views.job_views import *
from .views.candidate_views.application_views import *
from .views.candidate_views.interview_views import *
from .views.company_views.interview_views import *

urlpatterns = [

    path('login/', login_view, name='login'),
    path('logout/', logout_view, name='logout'),
    path('', login_view, name='home'),
    path('crm-admin/dashboard/', dashboard, name='dashboard'),
    path('company/dashboard/', company_dashboard, name='company_dashboard'),
    path('candidate/dashboard/', candidate_dashboard, name='candidate_dashboard'),
    
# admin dashboard
    path('candidates/', candidates_list, name='candidates_list'),
    path('candidates/add/', add_candidate, name='add_candidate'),
    path('candidates/<int:candidate_id>/', candidate_details, name='candidate_details'),
    path('candidates/<int:candidate_id>/edit/', edit_candidate, name='edit_candidate'),
    path('candidates/<int:candidate_id>/delete/', delete_candidate, name='delete_candidate'),

    path('companies/', companies_list, name='companies_list'),
    path('companies/add/', add_company, name='add_company'),
    path('companies/<int:company_id>/', company_details, name='company_details'),
    path('companies/<int:company_id>/edit/', edit_company, name='edit_company'),
    path('companies/<int:company_id>/delete/', delete_company, name='delete_company'),

    path('jobs/', jobs_list, name='jobs_list'),
    path('jobs/add/', add_job, name='add_job'),
    path('jobs/<int:job_id>/', job_details, name='job_details'),
    path('jobs/<int:job_id>/edit/', edit_job, name='edit_job'),
    path('jobs/<int:job_id>/delete/', delete_job, name='delete_job'),

    path('applications/', applications_list, name='applications_list'),
    path('applications/add/', add_application, name='add_application'),
    path('applications/<int:application_id>/', application_details, name='application_details'),
    path('applications/<int:application_id>/edit/', edit_application, name='edit_application'),
    path('applications/<int:application_id>/delete/', delete_application, name='delete_application'),
    path(
    'applications/<int:application_id>/move-next/',move_application_next_stage,
    name='move_application_next_stage'
    ),


    path('interviews/',interviews_list, name='interviews_list'),
    path('interviews/add/',add_interview, name='add_interview'),
    path('interviews/<int:interview_id>/',interview_details, name='interview_details'),
    path('interviews/<int:interview_id>/edit/',edit_interview, name='edit_interview'),
    path('interviews/<int:interview_id>/delete/',delete_interview, name='delete_interview'),

    path('evaluations/',evaluations_list, name='evaluations_list'),
    path('evaluations/add/',add_evaluation, name='add_evaluation'),
    path('evaluations/<int:evaluation_id>/',evaluation_details, name='evaluation_details'),
    path('evaluations/<int:evaluation_id>/edit/',edit_evaluation, name='edit_evaluation'),
    path('evaluations/<int:evaluation_id>/delete/',delete_evaluation, name='delete_evaluation'),

    path('activities/',activities_list, name='activities_list'),
    path('activities/add/',add_activity, name='add_activity'),
    path('activities/<int:activity_id>/',activity_details, name='activity_details'),
    path('activities/<int:activity_id>/edit/',edit_activity, name='edit_activity'),
    path('activities/<int:activity_id>/delete/',delete_activity, name='delete_activity'),

#Company dashboard
    path('company/jobs/', company_jobs_list, name='company_jobs_list'),
    path('company/jobs/add/', company_add_job, name='company_add_job'),
    path('company/jobs/<int:job_id>/edit/', company_edit_job, name='company_edit_job'),
    path('company/jobs/<int:job_id>/delete/', company_delete_job, name='company_delete_job'),
    path('company/jobs/<int:job_id>/', company_job_details, name='company_job_details'),
    path('company/applications/', company_applications_list, name='company_applications_list'),
    path('company/applications/<int:application_id>/', company_application_details, name='company_application_details'),
    path('company/interviews/', company_interviews_list, name='company_interviews_list'),
    path('company/applications/<int:application_id>/schedule-interview/', company_add_interview, name='company_add_interview'),
    path('company/interviews/<int:interview_id>/', company_interview_details, name='company_interview_details'),


#Candidate dashboard
    path('candidate/jobs/', candidate_jobs_list, name='candidate_jobs_list'),
    path('candidate/jobs/<int:job_id>/', candidate_job_details, name='candidate_job_details'),
    path('candidate/jobs/<int:job_id>/apply/', apply_to_job, name='apply_to_job'),
    path('candidate/applications/', candidate_applications_list, name='candidate_applications_list'),
    path('candidate/applications/<int:application_id>/', candidate_application_details, name='candidate_application_details'),
    path('candidate/interviews/', candidate_interviews_list, name='candidate_interviews_list'),
    path('candidate/interviews/<int:interview_id>/', candidate_interview_details, name='candidate_interview_details'),

]
