from django.conf.urls import patterns, include, url
from django.views.generic import TemplateView
from problems import views

urlpatterns = [
	url(r'^$', views.site_home, name='site_home'),
	url(r'^(?P<problem_number>\d+)(\..+)?/$', views.ProblemView.as_view(), name='euler_problem'),
]