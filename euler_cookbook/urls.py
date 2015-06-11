from django.conf.urls import patterns, include, url
from django.views.generic import TemplateView

urlpatterns = [
	url(r'^$', TemplateView.as_view(template_name="base.html"), name="site_home"),
    url(r'^sum_square_difference/', include('sum_square_difference.urls')),
    url(r'^counting_sundays/', include('counting_sundays.urls')),
]