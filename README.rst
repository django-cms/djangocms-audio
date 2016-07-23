################
django CMS Audio
################


|pypi| |build| |coverage|


This addon is an `Aldryn <http://aldryn.com>`_-compatible audio plugin for
`django CMS <http://django-cms.org>`_ and is available on the
`django CMS Marketplace
<https://marketplace.django-cms.org/en/addons/browse/djangocms-googlemap/>`_.

It allows you to upload a single file or an entire folder. The templates are
very simplistic by choice and we encourage you to adapt them to your
projects requirements.

.. image:: preview.gif


Contributing
============

This is a an open-source project. We'll be delighted to receive your
feedback in the form of issues and pull requests. Before submitting your
pull request, please review our `contribution guidelines
<http://docs.django-cms.org/en/latest/contributing/index.html>`_.

One of the easiest contribution is helping to translate this addon on
`Transifex <https://www.transifex.com/projects/p/djangocms-audio/>`_.


Requirements
============

* django CMS 3.2 or higher
* Django 1.8 or higher
* Python 2.7 / 3.3 or higher


Documentation
=============


Installation
------------

Please make sure all `Requirements`_ are satisfied.

For a manual install:

* run ``pip install djangocms-audio``
* add ``djangocms_audio`` to your ``INSTALLED_APPS``
* run ``python manage.py migrate djangocms_audio``


Configuration
-------------

This addon provides a ``standard`` template for all instances. You can add
additional template choices by adding the ``DJANGOCMS_AUDIO_TEMPLATES``
setting::

    TEMPLATE_CHOICES = [
        ('feature', _('Featured Version')),
    ]

You'll need to create the `feature` folder inside ``templates/djangocms_audio/``
otherwise you will get a *template does not exist* error. You can do this by
copying the ``standard`` folder inside that directory and rename it to
``feature``.


Running Tests
-------------

You can run the tests by executing::

    virtualenv env
    source env/bin/activate
    pip install -r tests/requirements.txt
    python runtests.py


.. |pypi| image:: https://badge.fury.io/py/djangocms-audio.svg
    :target: http://badge.fury.io/py/djangocms-audio
.. |build| image:: https://travis-ci.org/divio/djangocms-audio.svg?branch=master
    :target: https://travis-ci.org/divio/djangocms-video
.. |coverage| image:: https://coveralls.io/repos/github/divio/djangocms-audio/badge.svg?branch=master
    :target: https://coveralls.io/github/divio/djangocms-audio?branch=master


TODO
====

- What should be the default name for variables {{ instance }}
- why use ugettext instead of lazy on the return values?
- should it be "default" or "standard" for template sets
- How to pin requirements correctly (>=2.3?)
- Check strings in model labels, uppercase, lowercase whats the best practice
- add test suite
- get documentation guideline for how long that section should be until
  we start a docs section
