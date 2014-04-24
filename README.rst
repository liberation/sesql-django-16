================
SeSQL Django 1.6
================

SeSQL ORM backend for Django 1.6 using the transaction features bundled in
Django 1.6.

Usage
=====

Once the package installed, import the ``DjangoOrmAdapter`` class provided
by this package and instanciate it under the ``orm`` variable name in your
``sesql_config`` module.

::

  # In sesql_config.py
  from sesql_django_16 import DjangoOrmAdapter

  orm = DjangoOrmAdapter()
