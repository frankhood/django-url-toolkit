=====
Usage
=====

To use Django Url Toolkit in a project, add it to your `INSTALLED_APPS`:

.. code-block:: python

    INSTALLED_APPS = (
        ...
        'url_toolkit.apps.UrlToolkitConfig',
        ...
    )

Add Django Url Toolkit's URL patterns:

.. code-block:: python

    from url_toolkit import urls as url_toolkit_urls


    urlpatterns = [
        ...
        url(r'^', include(url_toolkit_urls)),
        ...
    ]
