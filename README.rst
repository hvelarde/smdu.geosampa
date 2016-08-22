**********************************************
Suporte para autenticação baseada na Senha Web
**********************************************

.. contents:: Conteúdo
   :depth: 2

Life, the Universe, and Everything
==================================

A `Senha Web`_ é um serviço de autenticação da Prefeitura do Municipio de São Paulo.

Este pacote integra autenticação baseada na `Senha Web`_ no Plone.

.. _`Senha Web`: http://www.prefeitura.sp.gov.br/cidade/secretarias/financas/servicos/senhaweb/index.php?p=4458

Mostly Harmless
===============

.. image:: http://img.shields.io/pypi/v/smdu.geosampa.svg
   :target: https://pypi.python.org/pypi/smdu.geosampa

.. image:: https://img.shields.io/travis/hvelarde/smdu.geosampa/master.svg
    :target: http://travis-ci.org/hvelarde/smdu.geosampa

.. image:: https://img.shields.io/coveralls/hvelarde/smdu.geosampa/master.svg
    :target: https://coveralls.io/r/hvelarde/smdu.geosampa

Don't Panic
===========

Installation
------------

To enable this package in a buildout-based installation:

#. Edit your buildout.cfg and add add the following to it::

    [buildout]
    ...
    eggs =
        smdu.geosampa

After updating the configuration you need to run ''bin/buildout'',
which will take care of updating your system.

Go to the 'Site Setup' page in a Plone site and click on the 'Add-ons' link.

Check the box next to ``smdu.geosampa`` and click the 'Activate' button.

How does it work
----------------

TBA.
