#!/usr/bin/env python

"""
setup.py file for SWIG mytest
"""

from distutils.core import setup, Extension


mytest_module = Extension('_mytest',
                           sources=['mytest_wrap.c', 'mytest.c'],
                           )

setup (name = 'mytest',
       version = '0.1',
       author      = "SWIG Docs",
       description = """Simple swig mytest from docs""",
       ext_modules = [mytest_module],
       py_modules = ["mytest"],
       )