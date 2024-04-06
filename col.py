#!/usr/bin/env python

annual = 2500000
infl = 6
years = 48

amountneeded = annual
for i in range(1, years) :
    print (f"{i} -> Rs.{amountneeded:.2f} -> ${amountneeded/82:.2f}")
    annual = annual + (annual * infl/100)
    amountneeded += annual
