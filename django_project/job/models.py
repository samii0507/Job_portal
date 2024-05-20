from django.db import models
from users.models import User
from company.models import Company
from resume.models import Resume
 

class Job(models.Model):
    job_type_choices = (
        ('Remote', 'Remote'),
        ('Onsite', 'Onsite'),
        ('Hybrid', 'Hybrid')
    )

    state_choices = (
        ('Karnataka', 'Karnataka'),
        ('Assam', 'Assam'),
        ('Gujarat', 'Gujarat'),
        ('Kashmir', 'Kashmir'),
        ('Tamil Nadu', 'Tamil Nadu'),
        ('Bihar', 'Bihar'),
        ('Uttar Pradesh', 'Uttar Pradesh')
    )

    industry_choices = (
        ('Technology', 'Technology'),
        ('Education', 'Education'),
        ('Transportation', 'Transportation'),
        ('Finance', 'Finance'),
        ('Healthcare', 'Healthcare'),
        ('Sports', 'Sports'),
        ('Energy', 'Energy')
    )
    
    title_choices = (
        ('Developer', 'Developer'),
        ('Consultant','Consultant'),
        ('Analyst' , 'Analyst'),
        ('Manager' , 'Manager'),
        ('UI/UX' , 'UI/UX'),
        ('Human Resource' , 'Human Resource'),
        ('Operations' , 'Operations')
    )

    user = models.ForeignKey(User, on_delete=models.CASCADE)
    company = models.ForeignKey(Company, on_delete=models.CASCADE) 
    title = models.CharField(max_length=100, choices = title_choices, null = True, blank = True)
    city = models.CharField(max_length=100)
    salary = models.PositiveIntegerField(default=35000)
    requirements = models.TextField()
    ideal_candidate = models.TextField()
    is_available = models.BooleanField(default=True)
    timestamp = models.DateTimeField(auto_now_add=True)
    industry = models.CharField(max_length=20, choices=industry_choices, null=True, blank=True)
    state = models.CharField(max_length=20, choices=state_choices, null=True, blank=True)
    job_type = models.CharField(max_length=20, choices=job_type_choices, null=True, blank=True)

    def __str__(self):
        return self.title

class ApplyJob(models.Model):
    status_choices = (
        ('Accepted', 'Accepted'), 
        ('Declined', 'Declined'), 
        ('Pending', 'Pending')
    )
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    job = models.ForeignKey(Job, on_delete=models.CASCADE)
    timestamp = models.DateTimeField(auto_now_add=True)
    status = models.CharField(max_length=20, choices=status_choices)
    