# -*- coding: utf-8 -*-

from django.conf.urls.defaults import *

from kobo.django.xmlrpc.views import XMLRPCHandlerFactory


__all__ = ( 'xmlrpc_patterns', )


xmlrpc_handler = XMLRPCHandlerFactory('nitrate_XMLRPC')

xmlrpc_patterns = patterns('',
    (r'xmlrpc/$', xmlrpc_handler)
)
