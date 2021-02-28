#!/usr/bin/env python

class MaximalSubSequence :
    def bruteForce(self, arr) :
        currMaxSum = 0
        maxLeft = -1
        maxRight = -1
        
        for left in range(len(arr)) :
            for right in range(left, len(arr)) :
                s = sum(arr[x] for x in range(left, right+1))
                if (s > currMaxSum) :
                    currMaxSum = s
                    maxLeft = left
                    maxRight = right

        return (maxLeft, maxRight, currMaxSum)

    def nsquare(self, arr) :
        currMaxSum = 0
        maxLeft = -1
        maxRight = -1
        
        for left in range(len(arr)) :
            s = 0
            for right in range(left, len(arr)) :
                s += arr[right]
                if (s > currMaxSum) :
                    currMaxSum = s
                    maxLeft = left
                    maxRight = right

        return (maxLeft, maxRight, currMaxSum)

    def anotherNSquare(self, arr) :
        currMaxSum = 0
        maxLeft = -1
        maxRight = -1
        
        cumArray = [];
        for i in range(len(arr)) :
            x = cumArray[i-1] if i > 0 else 0
            cumArray.append(x + arr[i])

        for left in range(len(arr)) :
            for right in range(left, len(arr)) :
                s = cumArray[right] - cumArray[left-1]
                if (s > currMaxSum) :
                    currMaxSum = s
                    maxLeft = left
                    maxRight = right

        return (maxLeft, maxRight, currMaxSum)

    def divAndConq(self, arr, left, right) :
        if (left > right) : return (-1, -1, 0)
        if (left == right) : return (left, right, arr[left])

        mid = int((left + right) / 2)
        maxLeftHalf = self.divAndConq(arr, left, mid)
        maxRightHalf = self.divAndConq(arr, mid+1, right)

        #finding maxToLeft and maxToRight and combining them
        s = 0
        maxToLeft = 0
        leftExtent = mid
        for i in range(mid, left, -1) :
            s += arr[i]
            if (s > maxToLeft) :
                maxToLeft = s
                leftExtent = i

        s = 0
        maxToRight = 0
        rightExtent = 0
        for i in range(mid+1, right) :
            s += arr[i]
            if (s > maxToRight) :
                maxToRight = s
                rightExtent = i

        maxMid = maxToLeft + maxToRight
        maxMidLeft = leftExtent
        maxMidRight = rightExtent

        theThreeRanges = [maxLeftHalf, maxRightHalf, (maxMidLeft, maxMidRight, maxMid)]
        theThreeRanges.sort(key=lambda x: x[2])
        return theThreeRanges[-1]
        

m = MaximalSubSequence()
arr = [-2, 1, -3, 4, -1, 2, 1, -5, 4]
print(m.bruteForce(arr))
print(m.nsquare(arr))
print(m.anotherNSquare(arr))
print(m.divAndConq(arr, 0, len(arr) - 1))
