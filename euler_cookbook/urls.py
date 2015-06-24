from django.conf.urls import include, url
from django.views.generic import TemplateView
from django.contrib import admin
from django.conf import settings

from rest_framework import routers, viewsets

from problems.serializers import UserViewSet, ProblemViewSet

# Routers provide an easy way of automatically determining the URL conf.
router = routers.DefaultRouter()
router.register(r'users', UserViewSet)
router.register(r'problems', ProblemViewSet)

urlpatterns = [
	url(r'^', include('problems.urls')),
	url(r'^accounts/', include('accounts.urls')),
	url(r'^api/', include(router.urls)),
	url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework')),
	url(r'^grappelli/', include('grappelli.urls')),
	url(r'^admin/', include(admin.site.urls)),
]

if settings.DEBUG is False:
	urlpatterns += (url(r'^static/(?P<path>.*)$', 'django.views.static.serve', {'document_root': settings.STATIC_ROOT}),)