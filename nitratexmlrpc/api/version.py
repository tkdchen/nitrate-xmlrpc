# -*- coding: utf-8 -*-


__all__ = (
    'get',
)


XMLRPC_VERSION = (1, 1, 0, 'final', 1)


def get(request):
    '''
    Description: Retrieve XMLRPC's version

    Params:      No parameters.

    Returns:     A list that represents the version.

    Example:
    >>> Version.get()
    '''

    return XMLRPC_VERSION
