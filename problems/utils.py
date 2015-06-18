# helper functions

def multiples_of_three_and_five(n):
	"""
	returns the sum of all the multiples of three and 5 less than the integer input n.
	"""
	return sum([i for i in range(n) if i % 3 == 0 or i % 5 == 0])



# problem 19
# translated from: http://www.javaproblems.com/2013/11/project-euler-problem-19-counting_27.html

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

	