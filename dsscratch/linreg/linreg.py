#!/usr/bin/env python

## Take some example data that converts celsius to farenheit and try to find the formula using 
## linear regression using gradient descent

import numpy as np

## Canned data using the known formula (which we try to reinvent using gradient descent)
def getExamples(n) :
    return np.array([[i*5.0, i*9.0 + 32] for i in range(n)])

def findFit(m, c, points) :
    epoch = 10000
    learnrate = 0.001
    size = len(points)

    while (epoch > 0) :
        epoch -= 1
        ## run through all examples
        for x, y in points :
            newM = m + learnrate * (2.0/size) * (x * (y - m*x - c))
            newC = c + learnrate * (2.0/size) * (y - m*x - c)
            m = newM
            c = newC
    return m, c



if __name__ == "__main__" :
    d = getExamples(30)
    m, c = findFit(1, -1, d)
    print (m, c)
    for x, y in d :
        #print (x, y, m*x + c)
        pass

