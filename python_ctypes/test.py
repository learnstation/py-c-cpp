#!/usr/bin/python
# -*- coding: utf-8 -*-
from ctypes import cdll # 首先导入 ctypes 模块的 windll 子模块
 
helloworld = cdll.LoadLibrary("libhelloworld.dll") # 使用 windll 模块的 LoadLibrary 导入动态链接库


r = helloworld.hello()
r = helloworld.world()
print(helloworld)
print(r)
print(dir(helloworld))
print(helloworld.__dict__)
