from django.shortcuts import render, HttpResponse, redirect
from django.contrib import messages
from .models import User
from ..jobs.models import Job
# Create your views here.
def index(request):
    return render(request, 'users/index.html')

def create_user(request):
    print(request.POST)
    if request.method != 'POST':
        return redirect('/')
    errors = User.objects.validate(request.POST)
    if len(errors) > 0:
        for error in errors:
            messages.error(request, error)
    user = User.objects.create_user(request.POST)
    request.session['user_id'] = user.id
    request.session['name'] = request.POST['first_name']
    return redirect('users:dashboard')

def login(request):
    if request.method != 'POST':
        return redirect('/')
    valid, response, name = User.objects.login(request.POST)
    if valid == True:
        request.session['user_id'] = response
        request.session['name'] = name
        return redirect('users:dashboard')
    else:
        messages.error(request,response)
    return redirect('/')
    
def logout(request):
    request.session.clear()
    return redirect('users:index')

def dashboard(request):
    context = {
        'user_info': User.objects.get(id=request.session['user_id']),
        'jobs' : Job.objects.all(),
        'my_jobs': Job.objects.filter(assignee_id=request.session['user_id'])
    }
    return render (request, 'users/dashboard.html', context)

def addjob(request):
    if 'user_id' not in request.session:
        return redirect('users:index')
    #this directs user to the add a job page.
    context = {
        'user_info': User.objects.get(id=request.session['user_id'])
    } 
    return render(request,'users/addajob.html', context)

def view(request, id):
    context = {
        'jobs' : Job.objects.get(id=id),
        'user_info': User.objects.get(id=request.session['user_id'])
    }
    return render(request, 'users/view.html', context)


def edit(request, job_id):
    context = {
        'edit_job' : Job.objects.get(id=job_id)
    }
    return render(request,'users/userquotes.html', context)
