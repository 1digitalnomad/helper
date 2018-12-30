from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.index, name="index"),
    url(r'^register$', views.create_user, name="create_user"),
    url(r'^login$', views.login, name="login"),
    url(r'^logout$', views.logout, name="logout"),
    url(r'^dashboard$', views.dashboard, name="dashboard"),
    url(r'^addjob$', views.addjob, name="addjob"),
    url(r'^(?P<id>\d+)/view$', views.view, name="view"),
    url(r'^(?P<job_id>\d+)/edit$', views.edit, name="edit")

]
