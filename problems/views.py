from django.shortcuts import render_to_response, get_object_or_404
from django.template import RequestContext
from django.views.generic import TemplateView

from problems.models import Problem

def site_home(request, template_name = 'base.html'):

	context = {
		'problems': Problem.objects.all(),
	}

	return render_to_response(template_name, context_instance=RequestContext(request, context))


class ProblemView(TemplateView):
    template_name = "problem.html"

    def get_context_data(self, **kwargs):
        context = super(ProblemView, self).get_context_data(**kwargs)
        problem = get_object_or_404(Problem, number=kwargs['problem_number'])
        context['problem'] = problem
        return context