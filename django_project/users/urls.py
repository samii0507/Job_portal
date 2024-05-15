from django.urls import path
from . import views

urlpatterns = [
    path('register_applicant/', views.register_applicant, name='register_applicant'),
    path('register_recruiter/', views.register_recruiter, name='register_recruiter'),
    path('login/', views.login_user, name='login'),
    path('logout/', views.logout_user, name='logout'),
]