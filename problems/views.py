import json
from datetime import datetime

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





"""
Ajax views for returning calculated values to the problem pages
"""

def problem_one(request):
	"""
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

	value = utils.multiples_of_three_and_five(number)

	content = {
		'number': number,
		'value': value,
		'last_requested': str(datetime.now())
	}
	return HttpResponse(json.dumps(content))


"""
Problem 6: Sum Square Difference

Simple view that expects a request in the format:
http://localhost:8000/difference?number=10 , where 10 is any natural number
"""
def get_sum_square_difference(request):

	n = int(request.GET.get('number', None))

	value = utils.calculate_difference(n)

	content = {
		'number': n,
		'value': value,
		'last_requested': str(datetime.now())
	}
	
	return HttpResponse(json.dumps(content))


"""
Problem 19: Counting Sundays
"""
weekdays = (
	(0, 'Sunday'),
	(1, 'Monday'),
	(2, 'Tuesday'),
	(3, 'Wednesday'),
	(4, 'Thursday'),
	(5, 'Friday'),
	(6, 'Saturday'),
)

@csrf_exempt
def calculate_days(request):
	body = json.loads(request.body)
	try:
		weekday = int(body.get('weekday'))
		day_of_month = int(body.get('day_of_month'))
		start_year = int(body.get('start_year'))
		end_year = int(body.get('end_year'))

	except KeyError:
		return HttpResponse('form error')

	content = {
		'weekday': weekdays[weekday][1],
		'day_of_month': day_of_month,
		'start_year': start_year,
		'end_year': end_year
	}
	content['num_days'] = utils.how_many(weekday, day_of_month, start_year, end_year)
	return HttpResponse(json.dumps(content))
