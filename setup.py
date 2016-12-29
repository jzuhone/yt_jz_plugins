#!/usr/bin/env python
from setuptools import setup
import numpy as np

setup(name='yt_jz_plugins',
      packages=['yt_jz_plugins'],
      version="0.1.0",
      description="John ZuHone's plugins for yt",
      author='John ZuHone',
      author_email='jzuhone@gmail.com',
      url='http://github.com/jzuhone/yt_jz_plugins',
      install_requires=["yt","numpy"],
      classifiers=[
          'Intended Audience :: Science/Research',
          'Operating System :: OS Independent',
          'Programming Language :: Python :: 2.7',
          'Programming Language :: Python :: 3.5',
          'Topic :: Scientific/Engineering :: Visualization',
      ],
      )
