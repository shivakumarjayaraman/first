#!/usr/bin/env python

## A stupid memoizing decorator
def memdec(f) :
    d = {}
    def inner(*args) :
        if args[0] in d : return d[args[0]]

        res = f(*args)
        d[args[0]] = res
        return res
    return inner



@memdec
def fib(n) :
    if (n <= 2) : return 1
    return fib(n-1) + fib(n-2)


for i in range(100) :
    print (i, fib(i))
