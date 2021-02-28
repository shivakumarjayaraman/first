#!/usr/bin/env python

def ap2(begin, step, end=None):
    res = type(begin + step) (begin)
    forever = end is None
    ind = 0
    while (forever or res < end) :
        yield res
        ind += 1
        res = begin + step * ind

