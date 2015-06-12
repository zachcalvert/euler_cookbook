from django.conf.urls import include, url
from django.views.generic import TemplateView
from django.contrib import admin

urlpatterns = [
	url(r'^', include('problems.urls')),
	url(r'^admin/', include(admin.site.urls)),
    url(r'^sum_square_difference/', include('sum_square_difference.urls')),
    url(r'^counting_sundays/', include('counting_sundays.urls')),
]