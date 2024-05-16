from django.urls import path
from . import views

urlpatterns = [
    path('update_resume/',views.update_resume,name='update_resume'),
    path('resume-details/',views.resume_details, name='resume-details'),
]