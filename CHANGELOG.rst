=========
Changelog
=========

1.1.1 (unreleased)
==================

* Fixed test matrix


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
