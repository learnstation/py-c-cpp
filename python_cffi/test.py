#!/usr/bin/python
# -*- coding: utf-8 -*-

from cffi import FFI
ffi = FFI()
ffi.cdef("""
int add(int a, int b);
int sub(int a, int b);
""")
lib = ffi.verify('#include "test.c"')
print lib.add(1,2)
