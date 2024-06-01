#!/usr/bin/env python

## fibonacci with memoizing .. ..
cache = {}

def fib(n) :
    global cache
    if (n in cache) :
        return cache[n]

    if (n <= 1) : return n
    ret = fib(n-1) + fib(n-2)
    cache[n] = ret
    return ret


for i in range(100) :
    print (i, fib(i))
