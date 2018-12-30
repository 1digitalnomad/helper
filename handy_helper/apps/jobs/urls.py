from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^(?P<job_id>\d+)/update$', views.update, name="update"),
    url(r'^(?P<job_id>\d+)/add_job$', views.add_job, name="add_job"),
    url(r'^(?P<job_id>\d+)/cancel$', views.destroy, name="destroy"),
    url(r'^create$', views.create, name="create")

]


