#!/usr/bin/env python

for i in range(1000, 10000) :
    a = int(i/1000)
    b = int ((i % 1000) / 100)
    c = int((i % 100) / 10)
    d = i % 10

    if ((a == b/2 ) and (b+c == 10) and (d == b+1) and (a+b+c+d == 23)) :
        print (a,b,c,d)
