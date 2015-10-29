from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^create_enterprise$', views.create_enterprise, name='create_enterprise'),
    url(r'^delete_enterprise$', views.delete_enterprise, name='delete_enterprise'),
    url(r'^(?P<enterprise_id>[0-9]+)/calification/$', views.calification, name='calification'),
    url(r'^crear_calification$', views.create_calification, name='create_calification'),
    url(r'^(?P<enterprise_id>[0-9]+)/delete_calification$', views.delete_calification, name='delete_calification'),
]