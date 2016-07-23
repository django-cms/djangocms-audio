################
django CMS Audio
################


|PyPI Version| |Build Status| |Coverage Status|


This addon is an `Aldryn <http://aldryn.com>`_-compatible audio plugin for
`django CMS <http://django-cms.org>`_. It provides the following plugins:

* Audio Player
  * Single file
  * Entire folder

.. image:: preview.gif


Contributing
============

This is a an open-source project. We'll be delighted to receive your 
feedback in the form of issues and pull requests. Before submitting your 
pull request, please review our `contribution guidelines 
<http://docs.django-cms.org/en/latest/contributing/index.html>`_.

If you want to help translate the plugin please do it on 
`Transifex <https://www.transifex.com/projects/p/djangocms-audio/>`_:


Requirements
============

* django CMS 3.2 or higher
* Django 1.8 or higher
* Python 2.7 / 3.3 or higher


Documentation
=============


Installation
------------

Please make sure all `Requirements`_ are statisfied. This addon is also 
available on the `django CMS Marketplace 
<https://marketplace.django-cms.org/en/addons/browse/djangocms-googlemap/>`_.

To install it manuall:

* run ``pip install djangocms-audio``
* add ``djangocms_audio`` to your ``INSTALLED_APPS``
* run ``python manage.py migrate djangocms_audio``


Running Tests
-------------

You can run the tests by using::

    virtualenv env
    source env/bin/activate
    pip install -r tests/requirements.txt
    python runtests.py


.. |PyPI_Version| image:: https://badge.fury.io/py/djangocms-audio.svg
    :target: http://badge.fury.io/py/djangocms-audio
.. |Build_Status| image:: https://travis-ci.org/divio/djangocms-audio.svg?branch=master
    :target: https://travis-ci.org/divio/djangocms-video
.. |Coverage_Status| image:: https://coveralls.io/repos/github/divio/djangocms-audio/badge.svg?branch=master
    :target: https://coveralls.io/github/divio/djangocms-audio?branch=master


TODO
====

- What should be the default name for variables {{ instance }}
- why use ugettext instead of lazy on the return values?
- should it be "default" or "standard" for template sets
- How to pin requirements correctly (>=2.3?)
- Check strings in model labels, uppercase, lowercase whats the best practice
- add test suite
- add screenshot to readme
- get documentation guideline for how long that section should be until
  we start a docs section
