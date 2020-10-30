#!/usr/bin/env python

from collections import defaultdict

d1 = list(range(1, 7))
d2 = list(range(1, 7))

freq = defaultdict(int)
for i in d1 :
    for j in d2 :
        freq[abs(i-j)] += 1

pdf = [float(freq[i])/36.0 for i in range(6)]

print (pdf)
print (sum(pdf))

exp = sum(x * i for i, x in enumerate(pdf))
print (exp)
