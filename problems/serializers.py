from django.contrib.auth.models import User

from rest_framework import serializers, viewsets

from models import Problem

class ProblemSerializer(serializers.HyperlinkedModelSerializer):
	class Meta: 
		model = Problem
		fields = ('number', 'title', 'description', 'solved', 'solution')
		extra_kwargs = {
            # 'url': {'lookup_field': 'number'}
            'problems': {'lookup_field': 'number'}
        }


# Serializers define the API representation.
class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ('url', 'username', 'email', 'is_staff')



# ViewSets define the view behavior.
class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer


class ProblemViewSet(viewsets.ModelViewSet):
    queryset = Problem.objects.all()
    serializer_class = ProblemSerializer