from django.contrib import admin
from django import forms

from problems.models import Problem

class ProblemForm(forms.ModelForm):
	description = forms.CharField(widget=forms.Textarea)
	solution = forms.CharField(widget=forms.Textarea)

	class Meta:
		model = Problem
		fields = '__all__'


class ProblemAdmin(admin.ModelAdmin):
    list_display = ('number', 'title', 'solved')
    form = ProblemForm

admin.site.register(Problem, ProblemAdmin)

