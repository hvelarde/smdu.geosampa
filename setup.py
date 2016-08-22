# -*- coding: utf-8 -*-
from setuptools import find_packages
from setuptools import setup

version = '1.0a1'
description = 'Plone integration with GeoSampa.'
long_description = (
    open('README.rst').read() + '\n' +
    open('CONTRIBUTORS.rst').read() + '\n' +
    open('CHANGES.rst').read()
)

setup(
    name='smdu.geosampa',
    version=version,
    description=description,
    long_description=long_description,
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Environment :: Web Environment',
        'Framework :: Plone',
        'Framework :: Plone :: 4.3',
        'Intended Audience :: System Administrators',
        'License :: OSI Approved :: GNU General Public License v2 (GPLv2)',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2.7',
        'Topic :: Software Development :: Libraries :: Python Modules',
    ],
    keywords='plone',
    author='Héctor Velarde',
    author_email='hector.velarde@gmail.com',
    url='https://github.com/hvelarde/smdu.geosampa',
    packages=find_packages('src'),
    package_dir={'': 'src'},
    namespace_packages=['smdu'],
    include_package_data=True,
    zip_safe=False,
    install_requires=[
        'plone.api',
        'plone.autoform',
        'plone.directives.form',
        'plone.formwidget.geolocation',
        'plone.formwidget.masterselect',
        'plone.namedfile',
        'plone.registry',
        'plone.supermodel',
        'Products.CMFCore',
        'Products.CMFPlone >=4.3',
        'Products.GenericSetup',
        'requests',
        'requests-mock',
        'setuptools',
        'z3c.form',
        'zope.component',
        'zope.i18nmessageid',
        'zope.interface',
        'zope.schema',
    ],
    extras_require={
        'test': [
            'AccessControl',
            'plone.app.robotframework',
            'plone.app.testing [robot]',
            'plone.browserlayer',
            'plone.testing',
            'robotsuite',
        ],
    },
    entry_points="""
    [z3c.autoinclude.plugin]
    target = plone
    """,
)
