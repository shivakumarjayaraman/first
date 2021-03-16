#!/usr/bin/env python

import math
import functools

X = [0.8, 0.1]

H = [[-1.0, 0.5], [0.1, 0.7]]
O = [[0.9, 0.5], [-0.3, -0.1]]

def sigmoid(x) :
    return 1.0/(1.0+math.exp(x*-1))

def dotprod(x, y) :
    return sum(xi * yi for xi, yi in zip(x, y))

def propagate(X, Y) :
    return [sigmoid(dotprod(X, y)) for y in Y]

def forward_prop(a, layers) :
    return functools.reduce(propagate, layers, a)

if __name__ == "__main__" :
    ##print (forward_prop(X, [H, O]))
    print (forward_prop([1, -1], [[[-1, 1], [1, 1]], [[1, 1], [-1, 1]]]))
