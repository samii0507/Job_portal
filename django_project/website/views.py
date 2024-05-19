from django.shortcuts import render
from job.models import Job ,ApplyJob

def home(request):
    return render(request, 'website/home.html')

def job_listing(request):
    jobs = Job.objects.filter(is_active=True).order_by('-timestamp')
    context = {
        'jobs': jobs
    }   
    return render(request, 'website/job_listing.html', context)
    
def job_detail(request, pk):
    if ApplyJob.objects.filter(user=request.user, job=pk).exists():
        has_applied = True
    else:
        has_applied = False
    job = Job.objects.get(pk=pk)
    context = {
        'job': job
    }
    return render(request, 'website/job_detail.html', context)