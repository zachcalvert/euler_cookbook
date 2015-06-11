# helper functions

def calculate_difference(n):
	return square_of_sums(n) - sum_of_squares(n)

def sum_of_squares(n):
	return sum([ i * i for i in xrange(1, n + 1) ])

def square_of_sums(n):
	return sum([ i for i in xrange(1, n + 1) ]) ** 2