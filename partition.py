#!/usr/bin/env python

import sys


def findSubset(l, n) :
    if (n < 0) :
        return []
    if (sum(l) == n) : 
        return l[:]
    if (sum(l) < n) :
        return []

    ## pop out last element
    last = l[-1]

    withLast = findSubset(l[0:len(l)-1], n-last)

    if (len(withLast) > 0) :
        withLast.append(last)
        return withLast

    return findSubset(l[0:len(l)-1], n)
    


if __name__ == "__main__" :
   numbs = [1, 5, 11 , 7]
   sumN = sum(numbs)
   if (sumN % 2 != 0) :
       print ("idiot cant partition")
       sys.exit(0)

   subs = findSubset(numbs, sum(numbs)//2)
   if (len(subs) == 0) :
       print ("oops cant partition")
       sys.exit(0)

   remaining = numbs[:]
   for i in subs :
       remaining.remove(i)
   print (subs, remaining)
