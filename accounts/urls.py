from django.conf.urls import include, url
urlpatterns = [
    url(
        r'^login/$',
        'django.contrib.auth.views.login',
        name='login',
        kwargs={'template_name': 'login.html'}
    ),
    url(
        r'^logout/$',
        'django.contrib.auth.views.logout',
        name='logout',
        kwargs={'next_page': '/'}
    ),
]