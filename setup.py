#!/usr/bin/env python

from distutils.core import setup

setup(name='TestExample',
      version='0.0.1',
      description='Simple Tornado app created to show how to test such apps',
      author='Wojciech Malinowski',
      author_email='wojciech.malinowski@gmail.com',
      url='https://github.com/wmalinowski/test-example',
      packages=['testexample'],
	  license='http://unlicense.org/',
	  install_requires=['tornado'],
     )
