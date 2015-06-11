# The Euler Cookbook

A django site with solutions to some of the problems posed on the Project Euler website.

## Setup

* git clone git@github.com:zachcalvert/euler_cookbook.git
* cd euler_cookbook
* mkvirtualenv euler
* pip install -r requirements.txt
* echo "create database euler_cookbook" | mysql -u root -p  (empty password)
* ./manage.py migrate
* ./manage.py runserver
* navigate to 'http://localhost:8000/' in a web browser

