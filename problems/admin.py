from django.contrib import admin
from django import forms

from problems.models import Problem, Contribution

class ProblemForm(forms.ModelForm):
	description = forms.CharField(widget=forms.Textarea)
	solution = forms.CharField(widget=forms.Textarea)

	class Meta:
		model = Problem
		fields = '__all__'


class ProblemAdmin(admin.ModelAdmin):
    list_display = ('number', 'title', 'solved')
    ordering = ('number',)
    form = ProblemForm

class ContributionAdmin(admin.ModelAdmin):
    list_display = ('submitted_by', 'problem')

admin.site.register(Problem, ProblemAdmin)
admin.site.register(Contribution, ContributionAdmin)

