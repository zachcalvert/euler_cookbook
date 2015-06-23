from datetime import datetime

def get_current_time():
	now = datetime.now()
	return now.strftime('%m-%d %H:%M:%S')

"""
Problem 1: Multiples of Three and Five
"""
def multiples_of_three_and_five(n):
	"""
	returns the sum of all the multiples of three and 5 less than the integer input n.
	"""
	return sum([i for i in range(n) if i % 3 == 0 or i % 5 == 0])


"""
Problem 2: Even Fibonacci Numbers
"""
def even_fibonacci_numbers(n):
	a, b = 1, 1
	total = 0
	while a <= n:
		if a % 2 == 0:
			total += a
		a, b = b, a+b
	return total



"""
Problem 4: Largest Palidrome Product
"""
def is_palindrome(num):
  return str(num) == str(num)[::-1]

def largest_palindrome_product(minimum, maximum):
	z = 0
	x_in = 0
	y_in = 0
	for x in range(maximum, minimum, -1):
		for y in range(maximum,minimum, -1):
			if is_palindrome(x*y):
				if x*y > z:
					z = x*y
					x_in = x
					y_in = y

	return '{0} ({1}*{2})'.format(z, x_in, y_in)


"""
Problem 6: Sum Square Difference
"""
def calculate_difference(n):
	return square_of_sums(n) - sum_of_squares(n)

def sum_of_squares(n):
	return sum([ i * i for i in xrange(1, n + 1) ])

def square_of_sums(n):
	return sum([ i for i in xrange(1, n + 1) ]) ** 2


"""
Problem 19: Counting Sundays
translated from: http://www.javaproblems.com/2013/11/project-euler-problem-19-counting_27.html
"""
def how_many(weekday, day_of_month, start_year, end_year):
	count = 0
	for y in range(start_year, end_year + 1):
		for m in range(1, 13):
			if day_of_week(y, m, day_of_month) == weekday:
				count +=1
	return count


def day_of_week(year, month, day):
	m = mod(month-3, 4800)
	y = mod(year +m/12, 400)
	m %= 12
	return (y + y/4 - y/100 + (13*m +2)/5 + day + 2) % 7


def mod(x, y):
	x %= y
	if (y > 0 and x < 0) or (y < 0 and x > 0):
		x += y
	return x

	