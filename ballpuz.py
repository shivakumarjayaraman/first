#!/usr/bin/env python
import math
from random import random

list = []
for i in range(20) :
    list.append('B')

for i in range(10) :
    list.append('R')

for i in range(29) :
    index = int(random() * 1000) % len(list)
    b1 = list.pop(index)
    index = int(random() * 1000) % len(list)
    b2 = list.pop(index)
    if (b1 == b2) :
        list.append('B')
        print ("Removing {} and {} . Adding B".format(b1, b2))
    else :
        list.append('R')
        print ("Removing {} and {} . Adding R".format(b1, b2))
print (list)
