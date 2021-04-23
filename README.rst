=============================
Django Url Tools
=============================

.. image:: https://badge.fury.io/py/django-url-toolkit.svg
    :target: https://badge.fury.io/py/django-url-toolkit

.. image:: https://travis-ci.org/frankhood/django-url-toolkit.svg?branch=master
    :target: https://travis-ci.org/frankhood/django-url-toolkit

.. image:: https://codecov.io/gh/frankhood/django-url-toolkit/branch/master/graph/badge.svg
    :target: https://codecov.io/gh/frankhood/django-url-toolkit

A useful toolkit to manage urls and absolute paths in your django project

Quickstart
----------

Install Django Url Tools::

    pip install django-url-toolkit

Add it to your `INSTALLED_APPS`:

.. code-block:: python

    INSTALLED_APPS = (
        ...
        'django_url_toolkit',
        ...
    )


Features
--------

* append_querystring
* get_current_site_absolute
* make_absolute_url
* static_absolute
* prepend_site

Example of usage
-------------
.. code-block:: python

    {% load url_toolkit %}'
    {% static_absolute 'test/fb.png' %}
    {{ '/test/fb.png'|prepend_site }}

Running Tests
-------------

Does the code actually work?

::

    source <YOURVIRTUALENV>/bin/activate
    (myenv) $ pip install tox
    (myenv) $ tox


Development commands
---------------------

::

    pip install -r requirements_dev.txt
    invoke -l


Credits
-------

Tools used in rendering this package:

*  Cookiecutter_
*  `cookiecutter-djangopackage`_

.. _Cookiecutter: https://github.com/audreyr/cookiecutter
.. _`cookiecutter-djangopackage`: https://github.com/pydanny/cookiecutter-djangopackage
