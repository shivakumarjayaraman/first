#!/usr/bin/env python

## Here’s an interesting question.. A college student visits Cisco Chennai for his campus interview which is on a Friday. Cisco gives him a ticket 
## back to his college town on Monday, so he gets to spend the weekend in Chennai. There are many things the candidate can do in Chennai in 2 days ..
##
## 1) Visit Marina beach (1/2 a day gone) : But rating is 7
## 2) Visit Mahabs (1 day gone) : But rating is 9
## 3) Visit the Egmore Museum (1/2 day) : Rating is 6
## 4) Shopping (Ranganathan St.. T. Nagar. Pondy Bazaar) for all 2 days : Rating is 9
## 5) Chennai heritage tour (St. Thomas Mt, Fort St. George, Mylapore, Santhome etc) : 1/2 day : Rating is 8
##
## What places should you visit, so you maximize your ratings, given your time constraints (2 days)
##

## Sites (indexed by place)
sites = ['Marina', 'Mahabs', 'Museum',  'Shopping', 'Heritage']

## Ratings (index by place)
ratings = [7, 9, 6,  9, 8]

## Time taken to visit in half days (also indexed by place)
duration=[1, 2, 1, 4, 1]

## The time intervals to construct a table (half days)
intervals = [1, 2, 3, 4]

maxRatings = [[0] * len(intervals) for i in range(len(sites))] 
selections = [[None] * len(intervals) for i in range(len(sites))]

for i in range(len(sites)) :
    timeToVisitSite = duration[i]
    for j in range(len(intervals)) :
        remainingTime = intervals[j] - timeToVisitSite
        ## maxRatings[i][j] is the maximized rating for sites[0..i] with a time available of intervals[j]
        if (remainingTime < 0) :
            if (i > 0) :
                maxRatings[i][j] = maxRatings[i-1][j]
                selections[i][j] = (i-1, j)
            else :
                maxRatings[i][j] = 0
                selections[i][j] = (-1, -1)

        else :
            rowAbove = maxRatings[i-1][j] if i > 0 else 0
            extraTimeRating = maxRatings[i-1][remainingTime-1] if (i > 0 and remainingTime > 0) else 0
            withSite = ratings[i] + extraTimeRating
            if (withSite > rowAbove) :
                if (i > 0 and remainingTime > 0) :
                    selections[i][j] = (i-1, remainingTime-1)
                else :
                    selections[i][j] = (-1, -1)
                maxRatings[i][j] = withSite
            else :
                maxRatings[i][j] = rowAbove
                selections[i][j] =  (i-1, j)


row, col = len(sites)-1, len(intervals)-1
print (maxRatings[row][col])
while (row >= 0) :
    nr, nc = selections[row][col]
    if (nc != col) :
        print (sites[row])
    row = nr
    col = nc



