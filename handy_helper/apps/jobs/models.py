from django.db import models
from ..users.models import User

# Create your models here.
class JobManager(models.Manager):
    def validate(self, form):
        errors = []
        if len(form['title']) <3:
            errors.append('Please enter title of job. Must be more than 3 characters.')
        if len(form['description']) <10:
            errors.append('Please add a description for the job. Must be more than 10 characters.')
        if len(form['location']) < 1:
            errors.append('Please enter the location of the job.')

        return errors


    def job_create(self, form_data):
        assignee = User.objects.get(id=form_data['helper'])
        print (assignee)
        self.create(
            title=form_data['title'],
            description=form_data['description'],
            location=form_data['location'],
            assignee_id = assignee,
            )

    def add_job(self, form_data, job_id):
        assignee = User.objects.get(id=form_data['helper'])
        job = Job.objects.get(id=job_id)
        print (form_data)
        
        job.title = form_data['title']
        job.description = form_data['description']
        job.location = form_data['location']
        job.assignee_id = assignee
        job.save()



    def delete_job(self, job_id):
        job = Job.objects.get(id=job_id)
        job.delete()

    def update(self, form_data, job_id):
        job = Job.objects.get(id=job_id)
        
        job.title = form_data['title'],
        job.description= form_data['description'],
        job.location = form_data['location']
        job.save()






class Job(models.Model):
    title = models.CharField(max_length=255)
    description = models.CharField(max_length=255)
    location = models.CharField(max_length=255)
    assignee_id = models.ForeignKey(User, related_name='myjobs')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    objects=JobManager()
