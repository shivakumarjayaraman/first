#!/usr/bin/env python

## You have an array of coins.. You are allowed to pick whatever coins you want
## but if you pick a particular coin, you cant pick the one adjacent to it
## Pick the maximum amount by following rules


def pickcoins(arr) :
    pickings = [0] * (len(arr) + 1)
    pickings[1] = arr[0]
    sel = [-1] * (len(arr) + 1)

    for i in range(2, len(arr) + 1) :
        withI  = arr[i-1] + pickings[i-2]
        withoutI = pickings[i-1]
        if (withI > withoutI) :
            pickings[i] = withI
            sel[i] = True
        else :
            pickings[i] = withoutI
            sel[i] = False

    return pickings, sel

    

coins = [5, 1, 2, 10, 6, 2]
print (coins)
maximum, sels = pickcoins(coins)
print (maximum)
## print the coins that were selected
selections = []
i = len(sels) - 1
while (i > 0) :
    if (sels[i]) :
        selections.append(coins[i-1])
        i = i-2
    else :
        i = i-1
print (selections)
        
