#!/usr/bin/env python

from one.two import B
from one.two.three import D

def foo() :
    print ("Inside A::foo")
    B.B()
    D.D()


def somefunc() :
    print ("Inside A::somefunc")

