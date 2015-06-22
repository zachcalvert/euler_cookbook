from rest_framework import serializers

from models import Problem

class ProblemSerializer(serializers.ModelSerializer):
	class Meta: 
		model = Problem
		fields = ('number', 'title', 'description', 'solved', 'solution')