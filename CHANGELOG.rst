=========
Changelog
=========

Unreleased
==========


2.1.1 (2023-07-04)
==================

* Remove requirement on django-treebeard.


2.1.0 (2023-06-29)
==================

* Added support for Django 4.2


2.0.0 (2020-09-02)
==================

* Added support for Django 3.1
* Dropped support for Python 2.7 and Python 3.4
* Dropped support for Django < 2.2


1.3.0 (2020-01-29)
==================

* Added support for Django 3.0
* Added further tests to raise coverage
* Fixed smaller issues found during testing


1.2.0 (2019-05-22)
==================

* Added support for Django 2.2 and django CMS 3.7
* Removed support for Django 2.0
* Extended test matrix
* Fixed typo in ``MANIFEST.in``
* Added isort and adapted imports
* Adapted code base to align with other supported addons


1.1.0 (2018-11-08)
==================

* Added support for Django 1.11, 2.0 and 2.1
* Removed support for Django 1.8, 1.9, 1.10
* Adapted testing infrastructure (tox/travis) to incorporate
  django CMS 3.5 and 4.0


1.0.2 (2016-11-22)
==================

* Prevent changes to ``DJANGOCMS_AUDIO_XXX`` settings from requiring new
  migrations
* Changed naming of ``Aldryn`` to ``Divio Cloud``
* Adapted testing infrastructure (tox/travis) to incorporate
  django CMS 3.4 and dropped 3.2


1.0.1 (2016-08-09)
==================

* Removed internal ``DEFAULT_CHOICE`` variable
* Removed ``base.html`` for performance reasons
* Fixed faulty settings parsing in aldryn_config.py
* Fixed typo in aldryn configuration
* Adapted private ``get_template`` method
* Updated translations


1.0.0 (2016-29-08)
==================

* Bumped to 1.0 as addon is released and used in production
* Changed the string representation for the <track> plugin
* Changed ``max_length`` to 255 as default
* Fixed a typo in the ``README.txt``
* Fixed missing includes / excludes in ``MANIFEST.in``
* Updated translations


0.1.2 (2016-08-08)
==================

* Fix issues with aldryn addon config input cleaning


0.1.1 (2016-08-08)
==================

* Fix issues with aldryn addon config


0.1.0 (unreleased)
==================

* Initial release
