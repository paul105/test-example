#!/usr/bin/env python

from distutils.core import setup

setup(name='TestExample',
      version='0.1.0',
      description='Simple Tornado app created to show how to test such apps',
      author='Wojciech Malinowski',
      author_email='wojciech.malinowski@gmail.com',
      url='https://github.com/wmalinowski/test-example',
      packages=['testexample'],
      license='http://unlicense.org/',
      install_requires=['tornado', 'babel'],
      package_data={'testexample': ['test/fixtures/*.json',
                                    'templates/*.html',
                                    'translations/*.csv']},
      scripts=['scripts/run_example_app.py'],
     )
