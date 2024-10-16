from django.shortcuts import get_object_or_404, render
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
import mimetypes
from django.views.generic import ListView, DetailView, CreateView, UpdateView
from django.urls import reverse_lazy

from .forms import JobApplicationForm
from .models import JobApplication


class JobApplicationListView(ListView):
    model = JobApplication
    template_name = 'dashboard.html'
    context_object_name = 'job_applications'

    def get_queryset(self):
        return JobApplication.objects.filter(user=self.request.user)


class JobApplicationDetailView(DetailView):
    model = JobApplication
    template_name = 'detailed_job_application.html'
    context_object_name = 'job_application'


class JobApplicationCreateView(CreateView):
    model = JobApplication
    template_name = 'form_job_application.html'
    form_class = JobApplicationForm
    success_url = reverse_lazy('jobapplication_list')

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)


class JobApplicationUpdateView(UpdateView):
    model = JobApplication
    template_name = 'form_job_application.html'
    form_class = JobApplicationForm
    success_url = reverse_lazy('jobapplication_list')

    def get_queryset(self):
        # Only allow the user to update their own job applications
        return JobApplication.objects.filter(user=self.request.user)


def download_doc(request, doc_type, application_id):
    job_application = get_object_or_404(JobApplication, id=application_id)

    # Open the file in binary mode
    if doc_type == 'cv':
        file = job_application.cv
    elif doc_type == 'cover':
        file = job_application.cover_letter
    file_path = file.path

    # Guess the file's mimetype
    mime_type, _ = mimetypes.guess_type(file_path)

    # Create the HTTP response with the file
    response = HttpResponse(file, content_type=mime_type)

    # Set the Content-Disposition header to force download
    response['Content-Disposition'] = f'attachment; filename={file.name}'

    return response
