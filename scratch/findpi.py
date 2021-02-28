#!/usr/bin/env python

import random
import math

def findpi(ndarts) :
    numInside = 0
    for i in range(ndarts) : 
        x = random.random() 
        y= random.random() 
        distance = math.sqrt(x*x + y*y)
        if (distance < 1) : 
            numInside += 1
    return 4 * numInside/ndarts


print (findpi(1000000))

