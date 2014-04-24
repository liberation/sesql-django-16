"""
Django 1.6 ORM for sesql
"""
import logging

from django.db import transaction

from sesql.orm.django.core import DjangoOrmAdapter

log = logging.getLogger('sesql')


class AtomicDjangoOrmAdapter(DjangoOrmAdapter):
    """
    ORM Adapater for Django 1.6
    """

    def transactional(self, function):
        """
        Wrap a function to have a sub-transaction-bound cursor
        """
        def transactional_inner(*args, **kwargs):
            nb_tries = 0
            transaction.set_autocommit(False)
            while nb_tries < self.NB_TRIES:
                cursor = self.begin()
                try:
                    with transaction.atomic():
                        res = function(cursor, *args, **kwargs)
                    return res
                except Exception, e:
                    nb_tries += 1
                    if nb_tries != self.NB_TRIES:
                        log.warning(
                            'function %s(%r, %r) failed with %s, '
                            're-attempting (#%d)' % (
                                function.__name__, args, kwargs, e, nb_tries))
                    else:
                        log.error(
                            'function %s(%r, %r) failed with %s, giving up' % (
                                function.__name__, args, kwargs, e))
                        raise
        transactional_inner.__name__ = function.__name__
        return transactional_inner


DjangoOrmAdapter = AtomicDjangoOrmAdapter
