#!/usr/bin/env python

## abs value of a number.. python has a built in abs, but hey no lib functs
def abs(x) :
    return x if x > 0 else -x

## check if answer is good enough to desired level of accuracy
def isGoodEnuf(n, r, x) :
    return abs(x**r - n) < 0.001

## Find rth root of n using Newton Raphson method
## if x is the rth root of n, then x^r = n .. 
## which means the answer is the solution to the eqn x^r - n = 0
## NR gives us a way to take a guess and find a better guess for a 
## equation's root (solution)
##
## So if f(x) = x^r -n, and we start with a guess 'g'
## betterGuess = guess - f(guess)/f'(guess) , where f'(x) is the 
## first derivative
## 
## f'(x) = d/dx(x^r - n), which is r*x^(r-1) ..
## this code just computes that until the answer is 'good enuf'
## 
def nThRoot(n, r) :
    guess = 1.0
    while not(isGoodEnuf(n, r, guess)) : 
        guess -= (guess**r - n)/(r*(guess**(r-1)))
    return guess

if __name__ == "__main__" :
    print (nThRoot(2, 2))
    print (nThRoot(3, 2))
    print (nThRoot(10, 3))
