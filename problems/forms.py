from django import forms

from problems.models import Contribution, Problem

class ContributionForm(forms.Form):
	name = forms.CharField(max_length=100,
            widget=forms.TextInput())
	problem = forms.ModelChoiceField(queryset=Problem.objects.filter(solved=False))

	solution = forms.CharField(widget=forms.Textarea)
	
	class Meta:
		model = Contribution
		fields = '__all__'