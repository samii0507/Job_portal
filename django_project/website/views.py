from django.shortcuts import render
from job.models import Job

def home(request):
    return render(request, 'website/home.html')

def job_listing(request):
    jobs = Job.objects.filter(is_active=True)
    context = {
        'jobs': jobs
    }   
    return render(request, 'website/job_listing.html', context)
    
