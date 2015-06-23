from django.conf.urls import include, url
from django.views.generic import TemplateView
from problems import views

urlpatterns = [
	url(r'^$', views.site_home, name='site_home'),
	url(r'^about/$', views.about, name='about'),
	url(r'^contribute/$', views.contribute, name='contribute'),
	url(r'^problem$', views.get_problem, name='get_problem'),

	url(r'^(?P<problem_number>\d+)(\..+)?/$', views.euler_problem, name='euler_problem'),
	url(r'^problem_one$', views.problem_one, name='problem_one'),
	url(r'^even_fibonacci_numbers$', views.get_even_fibonacci_numbers, name='get_even_fibonacci_numbers'),
	url(r'^sum_square_difference$', views.get_sum_square_difference, name='get_sum_square_difference'),
	url(r'^how_many_days/', views.calculate_days, name='calculate_days'),
]