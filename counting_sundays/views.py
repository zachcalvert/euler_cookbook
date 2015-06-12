import json 

from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt

from utils import how_many

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
	d['num_days'] = how_many(weekday, day_of_month, start_year, end_year)
	return HttpResponse(json.dumps(d))