from math import log
from collections import Counter

def calcEnt(dataset) :
    c = Counter([d[-1] for d in dataset])
    l = len(dataset)
    ent = [(i, -1 * (c[i]/l) * log(c[i]/l, 2)) for i in c]
    print (ent)
    return sum(e[1] for e in ent)


