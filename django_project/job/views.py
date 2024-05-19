from django.shortcuts import render,redirect
from .models import Job,ApplyJob
from .form import CreateJobForm,UpdateJobForm
from django.contrib import messages


#create a job
def create_job(request):
  if request.user.is_recruiter and request.user.has_company:
    if request.method == 'POST':
        form = CreateJobForm(request.POST)
        if form.is_valid():
            var = form.save(commit=False)
            var.user = request.user
            var.save()
            messages.info(request, 'Job created successfully')
            return redirect('dashboard')
        else:
            messages.warning(request, 'Error creating job')
            return redirect('create-job')
    else:
        form = CreateJobForm()
        context = {
            'form': form
        }
        return render(request, 'job/create_job.html', context)
  else:
       messages.warning(request, 'You are not authorized to view this page')
       return redirect('dashboard')
   
   
#update job
def update_job(request,pk):
    job = Job.objects.get(pk=pk)
    if request.method == 'POST':
        form = UpdateJobForm(request.POST)
        if form.is_valid():
            form.save()
            messages.info(request, 'Job updated successfully')
            return redirect('dashboard')
        else:
            messages.warning(request, 'Error updating job')
            return redirect('update-job', pk=pk)
    else:
        form = UpdateJobForm(instance=job)
        context = {
            'form': form
        }
        return render(request, 'job/update_job.html', context)

def manage_job(request):
    jobs = Job.objects.filter(user=request.user)
    context = {
        'jobs': jobs
    }
    return render(request, 'job/manage_job.html', context)

def apply_to_job(request,pk):
    if request.user.is_authenticated and request.user.is_applicant:
        job = Job.objects.get(pk=pk)
        if ApplyJob.objects.filter(user=request.user, job=job).exists():
            messages.warning(request, 'You have already applied to this job')
            return redirect('dashboard')
        else:
            ApplyJob.objects.create(
             user=request.user,
             job=job,
             status='Pending'
        )
        messages.info(request, 'Applied to job successfully')
        return redirect('dashboard')
        
    else:
        messages.info(request, 'You need to login to apply to job')
        return redirect('login')   
    
def all_applicants(request,pk):
    job = Job.objects.get(pk=pk)
    applicants = job.applujob_set.all()
    context = {
        'job': job,
        'applicants': applicants
    }
    return render(request, 'job/all_applicants.html', context)