def multiples_of_three_and_five(n):
	"""
	returns the sum of all the multiples of three and 5 less than the integer input n.
	"""
	return sum([i for i in range(n) if i % 3 == 0 or i % 5 == 0])