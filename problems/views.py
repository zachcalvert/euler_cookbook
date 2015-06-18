import json
from datetime import datetime

from django.views.decorators.csrf import csrf_exempt
from django.shortcuts import render_to_response, get_object_or_404
from django.template import RequestContext, TemplateDoesNotExist
from django.template.loader import get_template
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.http import HttpResponse

from problems.models import Problem
from problems import utils

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


# problem 19

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

	d = {
		'weekday': weekdays[weekday][1],
		'day_of_month': day_of_month,
		'start_year': start_year,
		'end_year': end_year
	}
	d['num_days'] = utils.how_many(weekday, day_of_month, start_year, end_year)
	return HttpResponse(json.dumps(d))
