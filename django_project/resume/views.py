from django.shortcuts import render,redirect
from django.contrib import messages
from .models import Resume
from users.models import User
from resume.forms import UpdateResumeForm
from job.models import ApplyJob
from job.views import _delete_application

#function to create/update resume
def update_resume(request):
    if request.user.is_authenticated and request.user.is_applicant and request.user.is_verified : #check so that recruiter cannot create a resume
        resume = Resume.objects.get(user=request.user)
        if request.method == 'POST' :
            form = UpdateResumeForm(request.POST, request.FILES, instance=resume)
            if form.is_valid():
                var = form.save(commit=False)
                user = User.objects.get(pk = request.user.id)
                user.has_resume = True
                user.save()
                var.save()
                messages.info(request, ' Your resume info has been updated.')
                return redirect('dashboard')
            else :
                messages.warning(request, 'Something went wrong')
        else :
            form = UpdateResumeForm(instance=resume)
            context = {'form':form}
            return render(request, 'resume/update_resume.html', context)
    else:
        messages.warning(request,'Permission denied') #denied recruiter to create a resume
        return redirect('dashboard')
    

#function to access resume details
def resume_details(request, pk):
    resume = Resume.objects.get(pk=pk)
    context = {'resume':resume}
    return render(request , 'resume/resume_details.html', context)

           
def _delete_resume(resume, user):
    applications = ApplyJob.objects.filter(user = user)
    for application in applications:
        _delete_application(resume, application.id)
    resume.delete()
    user.has_resume = False
    Resume.objects.create(user = user)
    user.save()

def delete_resume(request):
    if request.user.is_authenticated and request.user.is_applicant and request.user.is_verified and request.user.has_resume:
        user = request.user
        resume = Resume.objects.get(user = request.user)
        _delete_resume(resume,user)
        messages.warning(request, 'Your resume has been deleted')
        return redirect('dashboard')
    else:
        messages.warning(request, 'Permission Denied')
        return redirect('dashboard')