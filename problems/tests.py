from django.test import TestCase

# Create your tests here.

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