from django.urls import path
from . import views

urlpatterns = [
    path('update_company/', views.update_company, name='update_company'),
    path('company_details/<int:pk>/', views.company_details, name='company_details'),
]