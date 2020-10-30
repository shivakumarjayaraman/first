#!/usr/bin/env python

import random

## Throw n darts into a square of radius 2 
## and return the number of darts that fall inside the circle
def throwDarts(n) :
    ## generate two random numbers between -1 and 1
    ## if the distance from the origin is < 1, its inside 
    ## circle
    numberInside = 0
    for _ in range(n) :
        xcoord = random.uniform(-1, 1)
        ycoord = random.uniform(-1, 1)
        if (xcoord*xcoord + ycoord*ycoord < 1) :
            numberInside += 1
    return numberInside

## computePi
n = 1000000
numberInside = throwDarts(n)
print (numberInside*4/n)
    
