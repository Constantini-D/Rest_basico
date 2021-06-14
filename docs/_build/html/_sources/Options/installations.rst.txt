***********************
Startting the Program
***********************

To use rest framework you will need to have:

    *`Python Version <https://www.python.org/downloads/>`_ >= 3.5

    *`Django Version <https://docs.djangoproject.com/en/3.2/topics/install/>`_ >= 2.2


Starting with Django and Python
================================

To start your project you will need to install this following process:

.. code-block:: python

   pip install django

   django-admin startproject 'name of your projecjt' .

   django-admin startapp quickstart

   pip install djangorestframework

   pip install django-filter


And in your Django.Settings you will need to add ``rest_framework`` to the ``INSTALLED_APPS``

Sync the database for the first time
======================================

In the terminal you will migrate the database for the first time using the following code:

.. code-block:: python

   python manage.py migrate

Also, you will need to create a super user, that you allow you to enter as super user

.. code-block:: python

   python manage.py createsuperuser --email admin@example.com --username admin


After doing all this, we will start with the database of our application.
`Go to 'How to configurate my Database' <database.html>`_