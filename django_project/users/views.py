from django.shortcuts import render ,redirect
from django.contrib import messages
from django.contrib.auth import login, authenticate,logout
from .models import User
from .form import RegisterUserForm
from resume.models import Resume
from company.models import Company


def register_applicant(request):
    if request.method == 'POST':
        form = RegisterUserForm(request.POST)
        if form.is_valid():
            var = form.save(commit=False)
            var.is_applicant = True
            var.username = var.email
            var.save()
            Resume.objects.create(user=var)
            messages.info(request, 'You have successfully registered as an applicant')
            return redirect('login')
        else:
            messages.error(request, 'Something went wrong')
            return redirect('register_applicant')
    else:
        form = RegisterUserForm()
        context = {'form': form}
        return render(request, 'users/register_applicant.html', context)
    
 
 #Register recruiter    
def register_recruiter(request):
    if request.method == 'POST':
        form = RegisterUserForm(request.POST)
        if form.is_valid():
            var = form.save(commit=False)
            var.is_recruiter = True
            var.username = var.email
            var.save()
            Company.objects.create(user=var)
            messages.info(request, 'You have successfully registered as an applicant')
            return redirect('login')
        else:
            messages.error(request, 'Something went wrong')
            return redirect('register_recruiter')
    else:
        form = RegisterUserForm()
        context = {'form': form}
        return render(request, 'users/register_recruiter.html', context)


def login_user(request):
    if request.method == 'POST':
        email = request.POST('email')
        password = request.POST['password']
        user = authenticate(request, email=email, password=password)
        if user is not None and user.is_active:
            login(request, user)
            if user.is_applicant:
                return redirect('applicant_dashboard')
            elif user.is_recruiter:
                return redirect('recruiter_dashboard')
        else:
            messages.warning(request, 'Something Went wrong')
            return redirect('login')
    else:
        return render(request, 'users/login.html')
    
#logout user
def logout_user(request):
    logout(request)
    return redirect('login')