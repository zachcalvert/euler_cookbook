from datetime import datetime

def get_current_time():
    now = datetime.now()
    return now.strftime('%m-%d %H:%M:%S')


def valid_input(request):
    """
    helper function to yank the query arg out of request in the format
    '<request_path>?number=10'
    """
    number = request.GET.get('number', None)    

    # ensure a value is provided
    if not number:
        return HttpResponse('Please provide a value.', status=400)    

    # ensure the value is an integer
    try:
        number = int(number)
    except ValueError:
        return HttpResponse('Please provide an integer value.', status=400)    

    return number


def multiples_of_three_and_five(n):
    """
    Problem 1: Multiples of Three and Five
    """
    return sum([i for i in range(n) if i % 3 == 0 or i % 5 == 0])


def even_fibonacci_numbers(n):
    """
    Problem 2: Even Fibonacci Numbers
    """
    a, b = 1, 1
    total = 0
    while a <= n:
        if a % 2 == 0:
            total += a
            a, b = b, a+b
    return total


def largest_prime_factor(n):
    """
    Problem 3: Largest Prime Factor
    """
    i = 2
    while i * i < n:
        while n % i == 0:
            n = n / i
        i = i + 1    
    return n


def is_palindrome(num):
    return str(num) == str(num)[::-1]    

def largest_palindrome_product(minimum, maximum):
    """
    Problem 4: Largest Palidrome Product
    """
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



def calculate_difference(n):
    """
    Problem 4: Largest Palidrome Product
    """
    return square_of_sums(n) - sum_of_squares(n)    

def sum_of_squares(n):
    return sum([ i * i for i in xrange(1, n + 1) ])    

def square_of_sums(n):
    return sum([ i for i in xrange(1, n + 1) ]) ** 2


	