#!/usr/bin/env python

"""
setup.py file for SWIG mytest
"""

from distutils.core import setup, Extension

target = 'mytest'

mytest_module = Extension('_%s' % target,
                           sources=['%s_wrap.c' % target, '%s.c' % target],
                           )

setup (name = target,
       version = '0.1',
       author      = "SWIG Docs",
       description = """Simple swig mytest from docs""",
       ext_modules = [mytest_module],
       py_modules = [target],
       )