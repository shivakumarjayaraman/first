#!/usr/bin/env python

## Figure out the min ops it takes to reach a number 
## starting from 1 using ops +1, *2 and *3

ops = [0, 0] + [-1] * 10000
res = ["", "1"] + [""] * 10000
def opcount(n) :
    global ops, res

    if (ops[n] >= 0) :
        return ops[n]

    nminus1 = opcount(n-1)
    nby2 = opcount(int(n/2)) if (n % 2 == 0) else 10000
    nby3 = opcount(int(n/3)) if (n % 3 == 0) else 10000

    if ((nminus1 <= nby2) and (nminus1 <= nby3)) :
        res[n] = "(" + res[n-1] + " + 1" + ")"
        ops[n] = ops[n-1] + 1
    elif ((nby2 <= nminus1) and (nby2 <= nby3)) :
        res[n] = "(" + res[int(n/2)] + " * 2" + ")"
        ops[n] = ops[int(n/2)] + 1
    elif ((nby3 <= nminus1) and (nby3 <= nby2)) :
        res[n] = "(" + res[int(n/3)] + " * 3" + ")"
        ops[n] = ops[int(n/3)] + 1

    return ops[n]



for i in range(1, 15) :
    print ("Number of ops for ", i, " is ", opcount(i))
    print (i, " = ", res[i])
