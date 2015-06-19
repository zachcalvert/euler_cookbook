from django.conf.urls import include, url
from django.views.generic import TemplateView
from django.contrib import admin

urlpatterns = [
	url(r'^', include('problems.urls')),
	url(r'^admin/', include(admin.site.urls)),
]