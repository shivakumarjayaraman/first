#!/usr/bin/env python

## size of the chessboard on which we are placing queens
n=8

## is a given position attacked by a queen that has been placed so far
def isUnderAttack(i, j, arr) :
    for r, c in enumerate(arr) :
        if (j == c) or (r-c == i-j) or (r+c == i+j) :
            return True
    return False

## we pass around an array, ith element of which will contain
## the column number of the queen on the ith row.
def placeNextQueen(arr, i=0) :
    if (i == n) :
        return True
    for c in range(n) :
        if (not isUnderAttack(i, c, arr)) :
            arr.append(c)
            success = placeNextQueen(arr, i+1)
            if (success) :
                return True
            else :
                arr.pop()
    return False

def drawBoard(arr) :
    for i in range(n) :
        print ("-" * (2*n+1))
        for j in range(n) :
            if (j == arr[i]) :
                print ("|Q", end="")
            else :
                print ("| ", end="")
        print ("|")
    print ("-" * (2*n+1))
        

arr = []
if ( placeNextQueen(arr)) :
    drawBoard(arr)
else :
    print ("Not possible")

