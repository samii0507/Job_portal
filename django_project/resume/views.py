from django.shortcuts import render,redirect
from django.contrib import messages
from .models import Resume
from users.models import User
from .forms import UpdateResumeForm

def update_resume(request):
    if request.user.is_applicant:
        resume = Resume.objects.get(user=request.user)
        if request.method == 'POST':
            form = UpdateResumeForm(request.POST, instance=resume)
            if form.is_valid():
                var = form.save(commit=False)
                user = User.objects.get(id=request.user)
                user.has_resume = True
                var.save()
                user.save()
                messages.info(request,'Your resume is active now.You can start applying for jobs')
                return redirect('dashboard')
            else:
                messages.warning(request,'Something went wrong')
        else:
            form = UpdateResumeForm(instance=resume)
            context = {
                'form':form
            }
            return render(request,'resume/update_resume.html',context)
    else:
        messages.warning(request,'You are not authorized to view this page')
        return redirect('dashboard')

def resume_details(request,pk):
    resume = Resume.objects.get(pk=pk)
    context = {
        'resume':resume
    }
    return render(request,'resume/resume_details.html',context)