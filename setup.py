#!/usr/bin/env python
# -*- coding: utf-8 -*-
from setuptools import find_packages, setup

from djangocms_audio import __version__


REQUIREMENTS = [
    'django-cms>=3.2',
    'django-filer>=1.2',
    'djangocms-attributes-field>=0.1',
]


CLASSIFIERS = [
    'Development Status :: 5 - Production/Stable',
    'Environment :: Web Environment',
    'Framework :: Django',
    'Intended Audience :: Developers',
    'License :: OSI Approved :: BSD License',
    'Operating System :: OS Independent',
    'Programming Language :: Python',
    'Programming Language :: Python :: 2.7',
    'Programming Language :: Python :: 3',
    'Topic :: Internet :: WWW/HTTP',
    'Topic :: Internet :: WWW/HTTP :: Dynamic Content',
    'Topic :: Software Development :: Libraries :: Application Frameworks',
    'Topic :: Software Development :: Libraries :: Python Modules',
]


setup(
    name='djangocms-audio',
    version=__version__,
    author='Divio AG',
    author_email='info@divio.com',
    url='https://github.com/divio/djangocms-audio',
    license='BSD',
    description=('Adds audio plugin to django CMS.'),
    long_description=open('README.rst').read(),
    packages=find_packages(),
    include_package_data=True,
    zip_safe=False
    install_requires=REQUIREMENTS,
    classifiers=CLASSIFIERS,
    test_suite='test_settings.run',
)
