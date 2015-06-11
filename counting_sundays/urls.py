from django.conf.urls import patterns, include, url
from django.views.generic import TemplateView

import views

urlpatterns = [
	url(r'^$', TemplateView.as_view(template_name="counting_sundays.html"), name="counting_sundays_home"),
	url(r'^how_many_days/', views.calculate_days, name='calculate_days'),
]