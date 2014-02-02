#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
import sys


try:
    from setuptools import setup, find_packages
except ImportError:
    from distutils.core import setup, find_packages

with open('requirements.txt') as f:
    install_reqs = [line for line in f.read().split('\n') if line]
    tests_reqs = []

if sys.version_info < (2, 7):
    install_reqs += ['argparse']
    tests_reqs += ['unittest2']

import re
PACKAGEFILE = "{{ cookiecutter.repo_name }}/__init__.py"
file_content = open(PACKAGEFILE, "rt").read()


def regex(regex_expression, file_content):

    mo = re.search(regex_expression, file_content, re.M)
    if mo:
        return mo.group(1)
    else:
        raise RuntimeError("Unable to find version string in %s." % (PACKAGEFILE,))

def new_regex(regex_expression, file_content):

    regex_expression = r"^__{0}__ = ['\"]([^'\"]*)['\"]".format(regex_expression)
    mo = re.search(regex_expression, file_content, re.M)
    if mo:
        return mo.group(1)
    else:
        raise RuntimeError("Unable to find version string in %s." % (PACKAGEFILE,))


def pkg_metadata(attributes=[
    'title', 'package_name', 'author', 'description', 'email', 'version',
    'license', 'copyright']
):

    metadata = { k: new_regex(k, file_content) for k in attributes }
    return { k: v for k, v in metadata.items() if v }

__title__ = pkg_metadata()['title']
__package_name__ = pkg_metadata()['package_name']
__author__ = pkg_metadata()['author']
__description__ = pkg_metadata()['description']
__email__ = pkg_metadata()['email']
__version__ = pkg_metadata()['version']
__license__ = pkg_metadata()['license']
__copyright__ = pkg_metadata()['email']

if sys.argv[-1] == 'publish':
    os.system('python setup.py sdist upload')
    sys.exit()

if sys.argv[-1] == 'info':
    infos = {k.strip('__'): v for k, v in locals().items() if k.endswith('__') and k.startswith('__') and v}
    for k, v in infos.items():
        print('%s: %s' % (k, v))
    sys.exit()

readme = open('README.rst').read()
history = open('CHANGES').read().replace('.. :changelog:', '')

setup(
    name=__title__,
    version=__version__,
    description=__description__,
    long_description=readme + '\n\n' + history,
    author=__author__,
    author_email=__email__,
    url='https://github.com/{{ cookiecutter.github_username }}/{{ cookiecutter.repo_name }}',
    packages=find_packages(exclude=['docs']),
    include_package_data=True,
    install_requires=install_reqs,
    tests_require=tests_reqs,
    license=__license__,
    zip_safe=False,
    keywords=__title__,
    classifiers=[
        'Development Status :: 2 - Pre-Alpha',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: {{ cookiecutter.license }} License',
        'Natural Language :: English',
        "Programming Language :: Python :: 2",
        'Programming Language :: Python :: 2.6',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.3',
    ],
    test_suite='{{ cookiecutter.repo_name }}.testsuite',
)
