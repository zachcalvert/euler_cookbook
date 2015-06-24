import json
import requests
from bs4 import BeautifulSoup

from django.core.management.base import BaseCommand

from problems.models import Problem

class Command(BaseCommand):
    """
    Management command to load problem info from the euler cookbook API into a local db
    """
    def handle(self, *args, **options):
        for i in range(1,510):
            url = 'http://eulerscookbook.org/api/problems/{}/'.format(i)
            response = requests.get(url)
            content = json.loads(response.content)
            print(content)
            title = content.get('title')
            description = content.get('description')
            solved = content.get('solved')

            if solved:
                solution = content.get('solution')
            else:
                solution = None

            problem, created = Problem.objects.get_or_create(
                number=i,
                title=title,
                description=description,
                link='https://projecteuler.net/problem={}'.format(i),
                solved=solved,
                solution=solution
            )
            if created:
                print('added problem {0}: {1}'.format(i, title))