#!/usr/bin/env python

from math import sqrt
import itertools

class Vector :

    def __init__(self, *args) :
        self.contents = list(*args)

    def __iter__(self) :
        return iter(self.contents)

    def __repr__(self) :
        return f"Vector({self.contents})"

    def __abs__(self) :
        return sqrt(sum(x * x for x in self.contents))

    def __bool__(self) :
        return bool(abs(self))

    def __add__(self, other) :
        return Vector(a+b for a, b in itertools.zip_longest(self, other, fillvalue=0.0))

    def __radd__(self, other) :
        return self + other

    def __mul__(self, scalar) :
        return Vector(x * scalar for x in self)

    def __rmul__(self, scalar) :
        return Vector(x * scalar for x in self)

  

