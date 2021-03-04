#!/usr/bin/env python

class Tile :
    def __init__(self, initial) :
        self.state = []
        self.state.extend(initial)
        gap = [(row, col) for row in range(len(self.state)) for col in range(len(self.state[row])) if self.state[row][col] == -1]
        self.gap = gap[0]
        print (self.gap)

    def __eq__(self, other) :
        return self.state == other.state

    def clone(self) :
        return Tile(self.state)

    def nextstates(self) :
        tiles = []
        grow = self.gap[0]
        gcol = self.gap[1]

        if (grow > 0) :
            t1 = self.clone()
            t1[grow]

