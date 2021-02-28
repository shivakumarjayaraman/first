#!/usr/bin/env python

import numpy as np
import datetime


def vectorsum(n) :
    a = [i*i for i in range(n)]
    b = [i*i*i for i in range(n)]

    c = [x+y for x, y in zip(a, b)]
    return c

def numpysum(n) :
    a = np.arange(n) ** 2
    b = np.arange(n) ** 3
    return a+b


t1 = datetime.datetime.now()
x = vectorsum(20000)
t2 = datetime.datetime.now()
print ((t2-t1), " for vectorsum ", x[-2:])
t1 = datetime.datetime.now()
x = numpysum(20000)
t2 = datetime.datetime.now()
print ((t2-t1), " for numpysum ", x[-2:])


