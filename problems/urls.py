from django.conf.urls import include, url
from django.views.generic import TemplateView
from problems import views

urlpatterns = [
	url(r'^$', views.site_home, name='site_home'),
	url(r'^about/$', views.about, name='about'),
	url(r'^contribute/$', views.contribute, name='contribute'),

	url(r'^(?P<problem_number>\d+)(\..+)?/$', views.euler_problem, name='euler_problem'),

	url(r'^multiples_of_three_and_five$', views.get_multiples_of_three_and_five, 
		name='get_multiples_of_three_and_five'),

	url(r'^even_fibonacci_numbers$', views.get_even_fibonacci_numbers, 
		name='get_even_fibonacci_numbers'),

	url(r'^largest_prime_factor$', views.get_largest_prime_factor, 
		name='get_largest_prime_factor'),

	url(r'^largest_palindrome_product$', views.get_largest_palindrome_product, 
		name='get_largest_palindrome_product'),

	url(r'^sum_square_difference$', views.get_sum_square_difference, 
		name='get_sum_square_difference'),
	
	url(r'^how_many_days/', views.calculate_days, name='calculate_days'),
]