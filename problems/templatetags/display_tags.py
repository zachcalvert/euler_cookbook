from django import template
from django.core.urlresolvers import reverse

register = template.Library()


@register.filter
def previous_url(problem):
    previous_number = problem.number - 1
    return reverse('euler_problem', kwargs={'problem_number': previous_number})

@register.filter
def next_url(problem):
    next_number = problem.number + 1
    return reverse('euler_problem', kwargs={'problem_number': next_number})