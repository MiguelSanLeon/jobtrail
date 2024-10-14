from django.forms import ModelForm
from .models import JobApplication
from django.forms import DateInput, DateTimeInput, Textarea, URLInput

class JobApplicationForm(ModelForm):
    class Meta:
        model = JobApplication
        fields = [
            'job_title',
            'job_link_description',
            'application_posted',
            'date_applied',
            'date_last_followup',
            'recruiter_name',
            'recruiter_email',
            'manager_name',
            'manager_email',
            'company_name',
            'company_website',
            'status',
            'notes',
            'next_stage_date_time',
            'next_stage_prep',
            'cv',
            'cover_letter',
            ]
        
        widgets = {
            'job_link_description': URLInput(attrs={'placeholder': 'Enter job description URL'}),
            'application_posted': DateInput(attrs={'type': 'date'}),
            'date_applied': DateInput(attrs={'type': 'date'}),
            'date_last_followup': DateInput(attrs={'type': 'date'}),
            'next_stage_date_time': DateTimeInput(attrs={'type': 'datetime-local'}),
            'notes': Textarea(attrs={'rows': 3, 'placeholder': 'Additional notes about the application'}),
            'next_stage_prep': Textarea(attrs={'rows': 3, 'placeholder': 'Next stage preparation details'}),
        }