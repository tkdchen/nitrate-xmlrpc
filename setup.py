# -*- coding: utf-8 -*-

from setuptools import setup, find_packages


def get_version():
    return open('VERSION.txt', 'r').read().strip()

def get_long_description():
    readme = open('README.txt', 'r').read().strip()
    changes = open('CHANGES.txt', 'r').read().strip()
    return '%s\n%s' % (readme, changes)


setup(
    name='nitratexmlrpc',
    version=get_version(),
    author='Xuqing Kuang',
    author_email='xkuang@redhat.com',
    description='XMLRPC APIs for Nitrate',
    long_description=get_long_description(),
    url='https://github.com/<username>/nitrate.xmlrpc.git',
    license='GPLv2+',
    packages=find_packages(),
    keywords='kerberos nitrate xmlrpc',
    install_requires=[
        'kobo==0.3.6',
        'nitrate==0.1.0',
    ],
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Environment :: Web Environment',
        'Framework :: Django',
        'Intended Audience :: Customer Service',
        'Intended Audience :: Developers',
        'Intended Audience :: Information Technology',
        'Intended Audience :: System Administrators',
        'License :: OSI Approved :: GNU General Public License v2 or later (GPLv2+)',
        'Programming Language :: Python :: 2.7',
        'Topic :: Internet :: WWW/HTTP :: WSGI :: Application'
    ]
)
