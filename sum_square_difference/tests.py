from django.test import TestCase
from django.test import Client
from django.core.urlresolvers import reverse

from models import Calculation
from utils import calculate_difference, square_of_sums, sum_of_squares


class CalculationTest(TestCase):
	"""
	Ensure that our calculation utility functions work as expected
	"""

	def test_square_of_sums(self):
		"""
		The sum of the squares of the first 10 natural numbers is 3025 (given)
		"""
		self.assertEqual(square_of_sums(10), 3025)

	def test_sum_of_squares(self):
		"""
		The sum of the squares of the first 10 natural numbers is 385 (given)
		"""
		self.assertEqual(sum_of_squares(10), 385)

	def test_calculate_difference(self):
		"""
		The calculated difference between the above functions with input 10 is 2640 (given)
		"""
		self.assertEqual(calculate_difference(10), 2640)



def make_calculation(number):
	value = calculate_difference(number)
	c = Calculation.objects.create(number=number, value=value)
	return c

class ServiceTest(TestCase):
	def setUp(self):
		# Create Calculation instances for the first 5 integers
		for i in range(5):
			make_calculation(i)

	def test_service_endpoint(self):
		"""
		Ensure that the specified endpoint responds successfully and
		with the expected data
		"""
		response = self.client.get("%s?number=10" % reverse('get_difference'))
		self.assertEqual(response.status_code, 200)
		self.assertContains(response, '"number":10')
		self.assertContains(response, '"value":2640')
		self.assertContains(response, '"occurrences":1')

	def test_occurrences_incrementor(self):
		"""
		The number of occurrences for a given Calculation instance should 
		increase by 1 after a successful request to that resource
		"""
		count = Calculation.objects.get(number=1, value=0).occurrences
		response = self.client.get("%s?number=1" % reverse('get_difference'))
		self.assertEqual(response.status_code, 200)
		self.assertEqual(count+1, Calculation.objects.get(number=1).occurrences)

	def test_missing_arg(self):
		"""
		Verify that a request to the endpoint without a query arg fails
		in the expected way.
		"""
		response = self.client.get("%s?number=" % reverse('get_difference'))
		self.assertEqual(response.status_code, 400)
		# self.assertContains(response.content, 'Please provide a value.')

	def test_incorrect_arg_type(self):
		"""
		Verify that a request to the endpoint with a non-integer query arg fails
		in the expected way.
		"""
		response = self.client.get("%s?number=a" % reverse('get_difference'))
		self.assertEqual(response.status_code, 400)
		# self.assertContains(response, 'Please provide an integer value.')

