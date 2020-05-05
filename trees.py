#!/usr/bin/env python

## find the number of binary search trees possible with n nodes

def numTrees(n) :
    if (n == 0) : return 1
    if (n <= 2) : return n

    count = 0
    for i in range(1, n+1) :
        ## imagine i is root
        count += (numTrees(i-1) * numTrees(n-i))
    return count


for i in range(0, 10) :
    print (i, numTrees(i))
