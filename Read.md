Basic Django Application having CRUD operations
 
Setting the Virtual Environment

    python -m venv venv

Activate the virtual environment

	venv/scripts/activate

Installing Django dependencies

	py -m pip install Django

Initializing the Testapp Project

	django-admin startproject TestApp
	cd .\TestApp\
	py manage.py runserver

Adding employees app module

	py manage.py startapp employees


Change settings 

INSTALLED_APPS = [
    ...
    'django.contrib.staticfiles',
    'employees',
    ...
]

Add employees models then
    Py manage.py makemigrations employees
    Py manage.py migrate

To add Super User
    python manage.py createsuperuser

