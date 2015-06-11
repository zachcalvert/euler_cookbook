import json 

from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt

from utils import how_many


@csrf_exempt
def calculate_days(request):
	print(request.POST.get('day_of_month'))
	try:
		weekday = int(request.POST['weekday'])
		day_of_month = int(request.POST['day_of_month'])
		start_year = int(request.POST['start_year'])
		end_year = int(request.POST['end_year'])

	except KeyError:
		return HttpResponse('form error')

	d = {}
	d['num_days'] = how_many(weekday, day_of_month, start_year, end_year)
	return HttpResponse(json.dumps(d))