from django import forms
from .models import Resume

class UpdateResumeForm(forms.ModelForm):
    model = Resume
    exclude = ('user',)