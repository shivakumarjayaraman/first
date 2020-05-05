#!/usr/bin/env python

def genperm(l) :
    if (len(l) == 1) :
        return [l]

    first = l[0]
    perms = []
    for i in genperm(l[1:]) :
        for j in range(len(i)  + 1) :
            newl = i[:j]
            newl.append(first)
            newl.extend(i[j:])
            perms.append(newl)
    return perms


for i in genperm(['apple', 'peach', 'orange']) :
    print (i)

