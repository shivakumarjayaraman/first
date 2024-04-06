#!/usr/bin/env python

def isPerfect(n):
    sum = 0
    for i in range(1, n) :
        if (n%i == 0) : sum += i
    return (sum == n)


for i in range(1, 10000):
    if (isPerfect(i)) :
        print (i)
      
