#!/usr/bin/env python

def pow(a, n) :
    if (n == 0) : return 1
    temp = pow(a, int(n/2))
    return temp * temp * a if (n%2) else temp * temp


for i in range(20) :
    print (i, pow(2, i))
