from django.contrib import admin

from problems.models import Problem

class ProblemAdmin(admin.ModelAdmin):
    list_display = ('number', 'title', 'solved')

admin.site.register(Problem, ProblemAdmin)

