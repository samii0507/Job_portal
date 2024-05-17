from django.db import models
from company.models import Company
from users.models import User

class Job(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    comapny = models.ForeignKey(Company, on_delete=models.CASCADE)
    title = models.CharField(max_length=100)
    location = models.CharField(max_length=100)
    salary =models.PositiveIntegerField(default=35000)
    requirements = models.TextField()
    ideal_candidate = models.TextField()
    is_available = models.BooleanField(default=True)
    timestamp = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.title

class ApplyJob(models.Model):
    status_choices = (
        ('Accepted','Accepted'),
        ('Rejected','Rejected'),
        ('Pending','Pending')
    )
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    job = models.ForeignKey(Job, on_delete=models.CASCADE)
    timestamp = models.DateTimeField(auto_now_add=True)
    status = models.CharField(max_length=50,choices=status_choices,default='Pending')