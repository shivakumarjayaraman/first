#!/usr/bin/env python

sampleset = [[i, j, k] for i in range(1, 7) for j in range(1, 7) for k in range(1, 7)]

probs = [[0] * 4 for _ in range(4)]

for number_ones in range(4) :
    for number_threes in range(4) :
        filtered = [x for x in sampleset if x.count(1) == number_ones and x.count(3) == number_threes]
        probs[number_ones][number_threes] = len(filtered)

print ("Frequencies")
print ("------------")
for x in range(4):
    for y in range(4):
        print (f"{probs[x][y]:>5}", end="   ")
    print ("\n")

print ("Probabilities")
print ("------------")

for x in range(4):
    for y in range(4):
        print (f"{probs[x][y]/len(sampleset):.3f}", end="   ")
    print ("\n")
