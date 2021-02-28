#!/usr/bin/env python

class ArithmeticProgression :
    def __init__(self, begin, step, end=None) :
        self.begin = begin
        self.step = step
        self.end = end

    def __iter__(self) :
        res = type(self.begin + self.step)(self.begin)
        forever = self.end is None
        index = 0

        while forever or res < self.end :
            yield res
            index += 1
            res = self.begin + self.step * index
