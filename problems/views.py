from django.shortcuts import render_to_response, get_object_or_404
from django.template import RequestContext, TemplateDoesNotExist
from django.template.loader import get_template

from problems.models import Problem

def site_home(request, template_name = 'base.html'):

	context = {
		'problems': Problem.objects.all(),
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