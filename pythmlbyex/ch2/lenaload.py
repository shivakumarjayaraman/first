#!/usr/bin/env python
import numpy as np
import matplotlib.pyplot as plt

def lena():
    import pickle, os
    fname = os.path.join(os.path.dirname(__file__),'lena.dat')
    f = open(fname,'rb')
    lena = np.array(pickle.load(f))
    f.close()
    return lena

def blockMod4Indices(size):
    arr = np.arange(size)
    return arr %4 == 0

def show() :
    l = lena()
    acopy = l.copy()
    aview = l.view()
    
    xmax = l.shape[0]
    ymax = l.shape[1]
    #acopy[range(xmax), range(ymax)] = 0
    #acopy[range(xmax-1, -1, -1), range(ymax)] = 0

    ## fancy indexing


    plt.subplot(221)
    plt.imshow(acopy)
    #plt.imshow(np.hstack((l, acopy)))

    plt.subplot(222)
    acopy[blockMod4Indices(xmax), blockMod4Indices(ymax)] = 0
    acopy[(l > l.max()/4) & (l < 3*l.max()/4)] = 0
    plt.imshow(acopy)

    plt.show()

show()
