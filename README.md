Django Boilerplate
==================

A boilerplate for creating a django project in 5 mins.

Setup
-----
Follow the installation steps to get the boilerplate up and running.

### Dependencies
* [PIP](https://github.com/pypa/pip)

### Installation

Run the following commands:

    git clone https://github.com/argonemyth/django_boilerplate.git project_name 
    cd project_name
    $ virtualenv venv --distribute # if you use virtualenv, skip this if you don't.
    $ source ./venv/bin/activate # if you use virtualenv, skip this if you don't.
    pip install -r requirements/dev.txt
    python manage.py syncdb
    python manage.py migrate
    python manage.py runserver

Now, you just dive in and start developing your apps!
