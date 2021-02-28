#!/usr/bin/env python

## Implemention of a binary classifier using the WINNOW algorithm
import numpy as np

## training rate
numberOfFeatures = 3
alpha = 2
theta = numberOfFeatures-0.1

def fixW(w, lab, h, x) :
    if x == 0 : return w
    return (w*(alpha**(lab-h)))

## iteratively .. well recursively improve W so all examples are classified correctly
def improve(X, Y, W) :
    mistakes = 0

    for ex, lab  in zip(X, Y) :
        h = 1 if sum(ex*W)> theta  else 0
        print ("Trying example ", ex, lab, h)
        if (h == lab) : continue

        print ("Fixing weights")
        mistakes += 1

        ## adjust weights .. 
        ##print ([(w, x) for w, x in zip(W, ex)])
        W = [fixW(int(w), int(lab), int(h), int(x)) for w, x in zip(W, ex) ]
        print ("\t", W)
    
    print ("mistakes ", mistakes)
    if (mistakes == 0) : return W
    return improve(X, Y, W)


## learning examples
X = np.array([[1, 1, 1], [1, 1, 0], [1, 0, 1], [1, 0, 0], [0, 1, 1], [0, 1, 0], [0, 0, 1], [0, 0, 0]])
Y = np.array([1, 0, 0, 0, 1, 0, 0, 0])

## initial weights
W = np.array([1, 1, 1])

W = improve(X, Y, W)
print (W)

