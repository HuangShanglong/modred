#!/usr/bin/env python

from sys import version
# Check out unittest2, maybe use older pythons. Not 3 though.
if version < '2.7' or version > '3':
		raise ImportError('modaldecomp requires python version 2.7.x')
# Soon we will need to require numpy 1.7 for a change Jon will make
# in POD with new squeeze function.
from distutils.core import setup
setup(name='modred',
      version='0.1',
      author='Brandt Belson and Jonathan Tu',
      author_email='bbelson@princeton.edu, jhtu@princeton.edu',
      maintainer='Clancy Rowley',
      maintainer_email='cwrowley@princeton.edu',
      description='Compute modal decompositions and reduced-order models'+\
      		' easily, efficiently, and in parallel.',
      classifiers='',
      packages=['modred', 'modred.src', 'modred.tests'],
      package_dir={'modred':'', 'modred.src': 'src', 'modred.test': 'tests'},
      package_data={'modred':['tests/files_okid/SISO/*', 'tests/files_okid/SIMO/*', 
          'tests/files_okid/MISO/*', 'tests/files_okid/MIMO/*']},
      )
