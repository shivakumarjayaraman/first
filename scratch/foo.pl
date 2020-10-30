#!/usr/bin/env python
from functools import reduce
from collections import defaultdict

## Romans numbers are dumb.. Here's an equally dumb method to create a dict of romans
def makeRomans() :
    romans = ['', 'I', 'II', 'III', 'IV', 'V', 'VI', 'VII', 'VIII', 'IX', 'X']
    for i in range(11, 51) :
        if (i == 40) :
            romans.append('XL')
        elif (i == 50) :
            romans.append('L')
        else :
            msd = int(i/10)
            val = 'X' * msd if (msd != 4)  else 'XL'
            val += romans[i % 10]
            romans.append(val)
    return dict((v, n) for n, v in enumerate(romans))

def processInput() :
    count = int(input())
    names = [input() for _ in range(count)]
    namedict = defaultdict(list)
    for name in names :
        n, v = name.split()
        namedict[n].append(v)
    return namedict 


if __name__ == "__main__"  :
    romans = makeRomans()

    namemap = processInput()
    print ("------- Output----------")
    for name in sorted(namemap.keys()) :
        vals = namemap[name]
        for val in sorted(vals, key=lambda x : romans[x]) :
            print (f"{name} {val}")
