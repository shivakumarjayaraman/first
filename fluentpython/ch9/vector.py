#!/usr/bin/env python

from array import array
import math

class Vector2d :
    typecode = 'd'

    ## Alternate constructor
    @classmethod
    def frombytes(cls, octets) :
        typecode = chr(octets[0])
        memv = memoryview(octets[1:]).cast(typecode)
        return cls(*memv)

    def __init__(self, x, y) :
        self._x = float(x)
        self._y = float(y)

    @property
    def x(self) :
        return self._x

    @property
    def y(self) :
        return self._y

    def __iter__(self) :
        return (i for i in (self.x, self.y))

    def __repr__(self) :
        return f"{type(self).__name__}({self.x}, {self.y})"

    def __str__(self) :
        return str(tuple(self))

    def __bytes__(self) :
        return (bytes([ord(self.typecode)]) + bytes(array(self.typecode, self)))

    def __eq__(self, other) :
        return tuple(self) == tuple(other)

    def __abs__(self) :
        return math.hypot(self.x, self.y)

    def __bool__(self) :
        return bool(abs(self))

    def angle(self) :
        return math.atan2(self.y, self.x)

    def __format__(self, fmt_spec="") :
        if (fmt_spec.endswith('p')) :
            fmt_spec = fmt_spec[:-1]
            coords = (abs(self), self.angle())
        else :
            coords = tuple(self)

        comps = [format(c, fmt_spec) for c in coords]
        return f"({comps[0]}, {comps[1]})"

    def __hash__(self) :
        return hash(self.x) ^ hash(self.y)

