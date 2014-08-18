#!/usr/bin/env python

import os
import sys

try:
    from setuptools import setup
except ImportError:
    print "devsetup now needs setuptools in order to build. " \
          "Install it using your package manager (usually python-setuptools) or via pip (pip install setuptools)."
    sys.exit(1)

setup(name='dsbuild',
      version="0.1.0",
      description='System setup automation for developer',
      author="Stuart Herbert",
      author_email='stuart@stuartherbert.com',
      url='http://devsetup.systems/',
      license='New BSD',
      install_requires=['jinja2', "PyYAML", 'setuptools'],
      scripts=[
        "dsbuild",
        "dsbuild-template"
      ]
)
