import json
from datetime import datetime
from rest_framework.renderers import JSONRenderer

from django.views.decorators.csrf import csrf_exempt
from django.shortcuts import render_to_response, get_object_or_404, redirect
from django.template import RequestContext, TemplateDoesNotExist
from django.template.loader import get_template
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.http import HttpResponse
from django.contrib import messages
from django.utils.translation import ugettext_lazy as _

from problems.models import Problem, Contribution
from problems import utils
from problems.serializers import ProblemSerializer

from forms import ContributionForm

def site_home(request, template_name = 'base.html'):

    problems = Problem.objects.all()    

    paginator = Paginator(problems, 50)
    page = request.GET.get('page')    

    try:
        problems = paginator.page(page)
    except PageNotAnInteger:
        # If page is not an integer, deliver first page.
        problems = paginator.page(1)
    except EmptyPage:
    # If page is out of range (e.g. 9999), deliver last page of results.
        problems = paginator.page(paginator.num_pages)    

    context = {
        'problems': problems,
    }    

    return render_to_response(template_name, context_instance=RequestContext(request, context))


def about(request, template_name='about.html'):
    context = {}
    return render_to_response(template_name, context_instance=RequestContext(request, context))


def contribute(request, template_name='contribute.html'):
    title = 'Contribute'

    if request.method == 'POST':
        form = ContributionForm(data=request.POST)
        if form.is_valid():
            problem_id = form['problem'].value()
            problem = Problem.objects.get(id=problem_id)
            submitted_by = form['name']
            solution = form['solution']
            Contribution.objects.create(submitted_by=submitted_by, problem=problem, solution=solution)            

            messages.add_message(request, messages.SUCCESS,
            	_('Thanks for contributing! Your solution will be reviewed as soon as possible.'))        

        return redirect('site_home')
    else:
        form = ContributionForm(initial={})    

    context = {}
    context['form'] = form
    context['title'] = title    

    return render_to_response(template_name,
    context_instance=RequestContext(request, context))



def euler_problem(request, problem_number):
    template_name = "solutions/{}.html".format(problem_number)
    try:
        get_template(template_name)
    except TemplateDoesNotExist:
        template_name = "problem.html"    

    problem = get_object_or_404(Problem, number=problem_number)    

    context = {
        'problem': problem,
    }    

    return render_to_response(template_name, context_instance=RequestContext(request, context))


def get_multiples_of_three_and_five(request):
    """
    Problem 1: Multiples of Three and Five
    """
    number = utils.valid_input(request)    

    value = utils.multiples_of_three_and_five(number)    

    content = {
        'number': number,
        'value': value,
        'last_requested': utils.get_current_time()
    }
    return HttpResponse(json.dumps(content))


def get_even_fibonacci_numbers(request):
    """
    Problem 2: Even Fibonacci Numbers
    """
    number = utils.valid_input(request)    

    value = utils.even_fibonacci_numbers(number)    

    content = {
        'number': number,
        'value': value,
        'last_requested': utils.get_current_time()
    }
    return HttpResponse(json.dumps(content))


def get_largest_prime_factor(request):
    """
    Problem 3: Largest Prime Factor
    """
    number = utils.valid_input(request)    

    value = utils.largest_prime_factor(number)    

    content = {
        'number': number,
        'value': value,
        'last_requested': utils.get_current_time()
    }
    return HttpResponse(json.dumps(content))


def get_largest_palindrome_product(request):
    """
    Problem 4: Largest Palindrome Product
    http://localhost:8000/largest_palindrome_product?min=100&max=999
    """
    minimum = int(request.GET.get('min', None))
    maximum = int(request.GET.get('max', None))    

    value = utils.largest_palindrome_product(minimum, maximum)    

    content = {
        'min': minimum,
        'max': maximum,
        'value': value,
        'last_requested': utils.get_current_time()
    }
    return HttpResponse(json.dumps(content))



def get_sum_square_difference(request):
    """
    Problem 6: Sum Square Difference

    Simple view that expects a request in the format:
    http://localhost:8000/difference?number=10 , where 10 is any natural number
    """

    number = utils.valid_input(request)    

    value = utils.calculate_difference(number)    

    content = {
        'number': number,
        'value': value,
        'last_requested': utils.get_current_time()
    }    

    return HttpResponse(json.dumps(content))

