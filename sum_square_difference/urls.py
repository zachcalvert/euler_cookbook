from django.conf.urls import patterns, include, url
from django.views.generic import TemplateView

import views

urlpatterns = [
	url(r'^$', TemplateView.as_view(template_name="sum_square.html"), name="sum_square_home"),
    url(r'^difference$', views.get_sum_square_difference, name='get_sum_square_difference'),
]