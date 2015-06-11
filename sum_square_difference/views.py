from django.http import HttpResponse
from rest_framework.renderers import JSONRenderer

from models import Calculation
from serializers import CalculationSerializer
from utils import calculate_difference


"""
Simple view that expects a request in the format:

http://localhost:8000/difference?number=10 , where 10 is any natural number

Takes the given number and tries to find it in the db.
If the number is not found, the value is calculated and
the corresponding db entry is saved.
"""
def get_difference(request):

	number = request.GET.get('number', None)

	# ensure a value is provided
	if not number:
		return HttpResponse('Please provide a value.', status=400)

	# ensure the value is an integer
	try:
		number = int(number)
	except ValueError:
		return HttpResponse('Please provide an integer value.', status=400)

	try:
		c = Calculation.objects.get(number=number)
		c.occurrences += 1
		c.save()
    
	except Calculation.DoesNotExist:
		value = calculate_difference(number)
		c = Calculation.objects.create(number=number, value=value)
	
	# serialize the instance and return the data
	serializer = CalculationSerializer(c)
	content = JSONRenderer().render(serializer.data)
	return HttpResponse(content)
