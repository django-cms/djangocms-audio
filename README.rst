================
django CMS Audio
================


|pypi| |build| |coverage|

**django CMS Audio** is a set of plugins for `django CMS <http://django-cms.org>`_
that allow you to publish audio files on your site (using an HTML5 player by default,
but you can override this in your own templates if required).

It uses files managed by `Django Filer <https://github.com/divio/django-filer>`_.
The plugins allow you to select a single file or an entire folder of files.

This addon is compatible with `Aldryn <http://aldryn.com>`_ and is also available on the
`django CMS Marketplace <https://marketplace.django-cms.org/en/addons/browse/djangocms-googlemap/>`_
for easy installation.

.. image:: preview.gif


Contributing
============

This is a an open-source project. We'll be delighted to receive your
feedback in the form of issues and pull requests. Before submitting your
pull request, please review our `contribution guidelines
<http://docs.django-cms.org/en/latest/contributing/index.html>`_.

One of the easiest contributions you can make is helping to translate this addon on
`Transifex <https://www.transifex.com/projects/p/djangocms-audio/>`_.


Documentation
=============


See ``REQUIREMENTS`` in the `setup.py <https://github.com/divio/djangocms-audio/blob/master/setup.py>`_
file for additional dependencies:

* Python 2.7, 3.3 or higher
* Django 1.8 or higher


Installation
------------

For a manual install:

* run ``pip install djangocms-audio``
* add ``djangocms_audio`` to your ``INSTALLED_APPS``
* run ``python manage.py migrate djangocms_audio``


Configuration
-------------

Note that the provided templates are very minimal by design. You are encouraged
to adapt and override them to your project's requirements.

This addon provides a ``default`` template for all instances. You can provide
additional template choices by adding a ``DJANGOCMS_AUDIO_TEMPLATES``
setting::

    DJANGOCMS_AUDIO_TEMPLATES = [
        ('feature', _('Featured Version')),
    ]

You'll need to create the `feature` folder inside ``templates/djangocms_audio/``
otherwise you will get a *template does not exist* error. You can do this by
copying the ``standard`` folder inside that directory and renaming it to
``feature``.

``MP3`` and ``OGG`` files are allowed by default. We recommend using ``MP3``
as it's supported across all major browsers. You can change the default
setting by overriding::

    DJANGOCMS_AUDIO_ALLOWED_EXTENSIONS = ['mp3', 'ogg', 'wav']


Running Tests
-------------

You can run tests by executing::

    virtualenv env
    source env/bin/activate
    pip install -r tests/requirements.txt
    python setup.py test


.. |pypi| image:: https://badge.fury.io/py/djangocms-audio.svg
    :target: http://badge.fury.io/py/djangocms-audio
.. |build| image:: https://travis-ci.org/divio/djangocms-audio.svg?branch=master
    :target: https://travis-ci.org/divio/djangocms-video
.. |coverage| image:: https://codecov.io/gh/divio/djangocms-audio/branch/master/graph/badge.svg
    :target: https://codecov.io/gh/divio/djangocms-audio
