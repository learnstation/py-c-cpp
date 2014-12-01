#!/usr/bin/python
# -*- coding: utf-8 -*-
import sys
import math
import time
import threading
import tornado
import tornado.ioloop
import tornado.web


class MainHandler(tornado.web.RequestHandler):
    def get(self):
        self.write("Hello, world")

class IOLoopThread(threading.Thread):

    def __init__(self, *args, **kwargs):
        super(IOLoopThread, self).__init__()
        self.application1 = tornado.web.Application([
            (r"/", MainHandler),
        ])
        self.application2 = tornado.web.Application([
            (r"/", MainHandler),
        ])
        self.application1.listen(8000)
        self.application2.listen(8888)

    def run(self):
        tornado.ioloop.IOLoop.instance().start()


def main():
    import json
    import thread
    d = {'a': 1, 'b': 2}
    print("hello world form python")
    print(json.dumps(d))

    ioloopThread = IOLoopThread()
    ioloopThread.start()

def cp_python(n):
    result = 0
    for i in xrange(0,n):
        result += math.pow(1.1, (math.sin(i) + math.cos(i)))
    return result

def cp1_python(n):
    result = 0
    for i in xrange(0,n):
        for j in xrange(0, n):
            result += i * j
    return result

def cp_cpp():
    import numc
    import time
    for i in xrange(2):
        n = int(math.pow(10, i))
        print("====count=%d ========="%(n))
        t = time.time()
        result = numc.cp1(n)
        tc = time.time()-t
        print(result) 
        print("result=%f c++ =====%f" %(result, tc))

        t = time.time()
        result = cp1_python(n)
        tp = time.time()-t
        print(result)
        print("result=%f python =====%f" %(result, tp))
