# coding=UTF-8
#------------------------------------------------------------------------------
# Copyright (c) Acoular Development Team.
#------------------------------------------------------------------------------

from setuptools import setup
from os.path import join, abspath, dirname
import os

bf_version = "22.3"
bf_author = "Acoular Development Team"


# Get the long description from the relevant file
here = abspath(dirname(__file__))
with open(join(here, 'README.rst')) as f:
    long_description = f.read()


install_requires = list([
      'numba',
      'numpy<1.22',
      'setuptools',	
      'scipy>=1.1.0',
      'scikit-learn',
      'tables>=3.4.4',
      'traits>=6.0',
	])

setup_requires = list([
      'numba',
      'numpy<1.24',
      'setuptools',	
      'scipy>=1.1.0',
      'scikit-learn',
      'tables>=3.4.4',
      'traits>=6.0',
	])
    
setup(name="acoular", 
      version=bf_version, 
      description="Library for acoustic beamforming",
      long_description=long_description,
      license="BSD",
      author=bf_author,
      author_email="info@acoular.org",
      url="http://www.acoular.org",
      classifiers=[
      'Development Status :: 5 - Production/Stable',
      'Intended Audience :: Education',
      'Intended Audience :: Science/Research',
      'Topic :: Scientific/Engineering :: Physics',
      'License :: OSI Approved :: BSD License',
      'Programming Language :: Python :: 3.7',
      'Programming Language :: Python :: 3.8',
      'Programming Language :: Python :: 3.9',
      ],
      keywords='acoustic beamforming microphone array',
      packages = ['acoular','acoular.demo'],

      install_requires = install_requires,

      setup_requires = setup_requires,

      python_requires = '>=3.7, <=3.9',
      
      #scripts=[join('examples','acoular_demo.py')],
      include_package_data = True,
      package_data={'acoular': ['xml/*.xml'],
		    'acoular': ['tests/*.*']},
      #to solve numba compiler 
      zip_safe=False
)



