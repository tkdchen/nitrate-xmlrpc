.. contents:: Table of Contents

Introduction
============

nitrate-xmlrpc provides XMLRPC API for nitrate to allow external applications to
access test cases' information via scripts.

XMLRPC APIs are implemented in a standard django application.

Installation
============

You can install this package by issuing pip or easy_install.

::

    $ pip install nitrate-xmlrpc

Or, using following command,

::

    $ cd path/to/nitrate-xmlrpc
    $ python setup.py install

Usage
=====

To enable XMLRPC APIs is quite easy, just like any other django applications by
following 

URL configuration
-----------------

Add following code to nitrate's settings module, whichever you use. First of all,
import ``xmlrpc_patterns`` from nitratexmlrpc's urls module.

::

    from nitratexmlrpc.urls import xmlrpc_patterns

Then, add URL mapping into your urlpatterns.

::

    (r'^', include(xmlrpc_patterns))

``'^'`` is used due to I want to provide XMLRPC service by exposing URL like
this ``http://[domain]/xmlrpc/``. Change the regular expression to satisfy your
requirements. For example, client can call XMLRPC APIs through
``http://[domain]/api/xmlrpc/``, if server uses,

::

    (r'^api/$', include(xmlrpc_patterns))

Settings configuration
----------------------

By default, nitrate-xmlrpc provides all necessary settings to make XMLRPC work
well. You just need import all names from ``nitratexmlrpc.settings``.

::

    from nitratexmlrpc.settings import *
