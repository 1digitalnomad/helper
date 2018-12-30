from django.shortcuts import render,HttpResponse, redirect
from django.contrib import messages
from .models import Job
from ..users.models import User

# Create your views here.
def create(request):
    errors = Job.objects.validate(request.POST)
    if len(errors) > 0:
        for error in errors:
            messages.error(request, error)
        return redirect('users:addjob')
    Job.objects.job_create(request.POST)
    return redirect ('users:dashboard')

    # return redirect(request, 'users/addajob.html')

    
def add(request, job_id):
    if 'user_id' not in request.session:
        return redirect('users:index')
    if request.method != 'POST':
        return redirect('users:index')
    errors = Job.objects.validate(request.POST)
    if errors:
        for error in errors:
            messages.error(request, error)
        return redirect('users:edit')
    Job.objects.add_job(request.POST, job_id)
    return redirect('users:dashboard')


def update(request, job_id):
    if 'user_id' not in request.session:
        return redirect ('users:index')
    if request.method != 'POST':
        return redirect('users:index')
    errors = Job.objects.validate(request.POST)
    if errors:
        for error in errors:
            messages.error(request, error)
        return redirect('users:edit')
    Job.objects.update(request.POST, job_id)
    return redirect('users:dashboard')


def add_job(request, job_id):
    if 'user_id' not in request.session:
        return redirect('users:index')
    if request.method != 'POST':
        return redirect('users:index')
    errors = Job.objects.validate(request.POST)
    if errors:
        for error in errors:
            messages.error(request, error)
        return redirect('users:edit')
    Job.objects.add_job(request.POST, job_id)
    return redirect('users:dashboard')


def destroy(request, job_id):
    Job.objects.delete_job(job_id)
    return redirect('users:dashboard')
    
