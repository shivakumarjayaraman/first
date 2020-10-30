#!/usr/bin/python

import math

## Find circular primes of lengths 2, 3, 4, 5, 6

def isPrime(n) :
    if (n == 2) : return True
    for i in range(2, int(math.sqrt(n)) + 1) :
        if (n % i == 0) : return False
    return True

def isCircularPrime(n) :
    len  = int(math.ceil(math.log(n+1, 10)))
    for i in range(len) :
        a, b = divmod(n, 10**(len-1))
        n = (b * 10 + a)
        if (isPrime(n) == False) : return False
    return True

for i in range(2, 7) :
    print ("Circular Primes of length ", i)
    smallest = 10 ** (i-1)
    largestPlusOne = (10 ** i)

    for n in range(smallest, largestPlusOne) :
        if isCircularPrime(n) :
            print ("    {}".format(n))
