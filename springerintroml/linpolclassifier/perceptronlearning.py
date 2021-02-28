#!/usr/bin/env python

## Implemention of a binary classifier using the perceptron classifier algorithm
import numpy as np

## training rate
alpha = 0.5

## iteratively .. well recursively improve W so all examples are classified correctly
def improve(X, Y, W) :
    mistakes = 0
    print (W)

    for ex, lab  in zip(X, Y) :
        ex = np.insert(ex, 0, 1)
        h = 1 if sum(ex*W)> 0  else 0
        if (h != lab) : 
            mistakes += 1

        ## adjust weights .. 
        W = [w + x*alpha*(lab-h) for w, x in zip(W, ex)]
        print ("\t", ex, lab, h)
        print ("\t\t", W)
    
    print ("mistakes ", mistakes)
    if (mistakes == 0) : return W
    return improve(X, Y, W)


## learning examples
X = np.array([[1, 0], [1, 1], [0, 0]])
Y = np.array([0, 1, 0])

## initial weights
W = np.array([0.1, 0.3, 0.4])

W = improve(X, Y, W)
print (W)

