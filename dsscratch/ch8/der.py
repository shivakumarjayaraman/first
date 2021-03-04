#!/usr/bin/env python

import matplotlib.pyplot as plt
from functools import partial
import random
import math

def diff_quotient(f, x, h) :
    return (f(x+h) - f(x))/h

def square(x) :
    return x*x

def derivative(x) :
    return 2*x

def partial_diff_quotient(f, v, i, h) :
    w = [v_j + (h if j == i else 0) for j, vj in enumerate(v)]
    return (f(w) - f(v))/h

def est_gradient(f, v, h=0.00001) :
    return [partial_diff_quotient(f, v, i, h) for i, _ in enumerate(v)]

def step(v, direction, step_size) :
    return [v_i + (dir_i*step_size)for v_i, dir_i in zip(v, direction)]

def sum_of_squares_gradient(v) :
    return [2*v_i for v_i in v]

def distance(a, b) :
    return math.sqrt(sum((ai - bi)*(ai-bi) for ai, bi in zip(a, b)))

def showConvergence() :
    v = [random.randint(-10, 10) for i in range(3)]
    print (v)
    tolerance = 0.0000001
    while (True) :
        gradient = sum_of_squares_gradient(v)
        next_v = step(v, gradient, -0.01)
        if (distance(next_v, v) < tolerance) :
            break
        v = next_v
    print (v)



def plotDerAndEst() :
    x = range(-100, 100)
    plt.title("Actual vs Numerical derivatives")
    plt.plot(x, list(map(derivative, x)), 'rx', label='Actual')
    plt.plot(x, list(map(partial(diff_quotient, square, h=0.00001), x)), 'b+', label='Numerical')

    ##plt.legend(loc=90)
    plt.show()

if __name__ == "__main__" :
    plotDerAndEst()
