from django.conf.urls import patterns, url

from . import views

urlpatterns = patterns('',
                       url(r'^$', views.index, name="index"),
                       url(r'^add/$', views.add, name="add"),
                       url(r'^(?P<snippet_id>\d+)/delete/$', views.delete,
                           name="delete"),
                       url(r'^(?P<snippet_id>\d+)/edit/$', views.edit,
                           name="edit"),
                       )
