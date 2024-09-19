#!/usr/bin/env python

def pi(numb):
    sign = 1.0
    pi = 0
    for i in range(numb+1) : 
        pi += sign * 1.0/(2*i + 1) 
        sign *= -1
    return 4*pi


if __name__ == "__main__" :
    print (pi(1000))

