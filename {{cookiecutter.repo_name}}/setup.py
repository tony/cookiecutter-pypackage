#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
import sys


try:
    from setuptools import setup, find_packages
except ImportError:
    from distutils.core import setup, find_packages

sys.path.insert(0, os.getcwd())  # we want to grab this:
from package_metadata import p

with open('requirements.txt') as f:
    install_reqs = [line for line in f.read().split('\n') if line]
    tests_reqs = []

if sys.version_info < (2, 7):
    install_reqs += ['argparse']
    tests_reqs += ['unittest2']

if sys.argv[-1] == 'publish':
    os.system('python setup.py sdist upload')
    sys.exit()

if sys.argv[-1] == 'info':
    for k, v in p.items():
        print('%s: %s' % (k, v))
    sys.exit()

readme = open('README.rst').read()
history = open('CHANGES').read().replace('.. :changelog:', '')

setup(
    name=p.title,
    version=p.version,
    description=p.description,
    long_description=readme + '\n\n' + history,
    author=p.author,
    author_email=p.email,
    url='https://github.com/{{ cookiecutter.github_username }}/{{ cookiecutter.repo_name }}',
    packages=find_packages(exclude=['docs']),
    include_package_data=True,
    install_requires=install_reqs,
    tests_require=tests_reqs,
    license=p.license,
    zip_safe=False,
    keywords=p.title,
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
