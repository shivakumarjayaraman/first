#!/usr/bin/env python

def genperm(x) :
    if (len(x) == 1) : return (x)
    return (x[i] + str for i in range(len(x)) 
           for str in genperm("".join(x[:i] + x[i+1:])))

print (list(genperm("abc")))
