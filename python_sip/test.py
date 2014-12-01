#!/usr/bin/python
# -*- coding: utf-8 -*-
import mymath

def ftime(repeat=10, number=1):
    import functools
    def fwrapper(func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            import sys
            import time
            if sys.platform == "win32":
                # On Windows, the best timer is time.clock()
                default_timer = time.clock
            else:
                # On most other platforms the best timer is time.time()
                default_timer = time.time
            r = []
            for i in xrange(repeat):
                start = default_timer()
                for x in xrange(number):
                    ret = func(*args, **kwargs)
                r.append(default_timer() - start)
            precision = 5
            best = min(r)
            print("*" * 10 + func.func_name + '*' * 10)
            print("raw times:", " ".join(["%.*g" % (precision, x) for x in r]))
            print("Repeat: %d, %d loops per repeat," % (repeat, number))
            usec = best * 1e6 / number
            if usec < 1000:
                print("Best of %d: %.*g usec per loop" % (repeat, precision, usec))
            else:
                msec = usec / 1000
                if msec < 1000:
                    print("Best of %d: %.*g msec per loop" % (repeat, precision, msec))
                else:
                    sec = msec / 1000
                    print("Best of %d: %.*g sec per loop" % (repeat, precision, sec))
            print("*" * 20)
            return ret, usec
        return wrapper
    return fwrapper

def add(a, b, count):
    ret = 0
    for x in xrange(count):
        ret += a + b
    return ret

@ftime()
def test(a, b, count):
    """Stupid test function"""
    mymath.add(a, b, count)

@ftime()
def test2(a, b, count):
    add(a, b, count)

if __name__ == '__main__':
    count = 10
    ret , usec= test(1, 2, count)
    ret1, usec1= test2(1, 2, count)
    print ret == ret1
    print usec1 / usec
