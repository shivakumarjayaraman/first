#!/usr/bin/env python

def findJump(dest, jmp, l, maxHops) :
    if (len(l) > maxHops) :
        return []

    if (dest == sum(l)) :
        return l

    l1 = l[:]
    l2 = l[:]
    l1.append(jmp+1)
    l2.append(-(jmp+1))

    ret = findJump(dest, jmp+1, l1, maxHops)
    if (len(ret) > 0) :
        return ret
    return findJump(dest, jmp+1, l2, maxHops)

maxHops = 30
for i in range(1, 100) :
    ## Try to find way to reach i using hops of len 1 .. 10
    for hops in range(1, maxHops) :
        l = findJump(i, 0, [], hops)
        if (len(l) > 0) :
            print ("Dest ", i, l)
            break

