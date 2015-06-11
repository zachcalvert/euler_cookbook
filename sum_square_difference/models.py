from django.db import models

class Calculation(models.Model):
	"""
	A class that represents the calculation of the difference between
	the sum of the squares of a given number, and the square of the sum
	the same number.

	We persist the calculation for a given number to avoid making the same 
	computation twice.
	"""
	last_requested = models.DateTimeField(auto_now=True)
	number = models.IntegerField(unique=True)
	value = models.IntegerField()
	occurrences = models.IntegerField(default=1)

	def __str__(self):
		return 'the calculated difference with {0} as input is: {1}'.format(self.number, self.value)