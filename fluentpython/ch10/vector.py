#!/usr/bin/env python

from array import array
import reprlib
import math
import numbers
import functools
import operator

class Vector:
    typecode = 'd'

    def __init__(self, components) :
        self._components = array(self.typecode, components)

    def __iter__(self) :
        return iter(self._components)

    def __repr__(self) :
        components = reprlib.repr(self._components)
        components = components[components.find("["):-1]
        return f"Vector({components})"

    def __str__(self) :
        return str(tuple(self))

    def __eq__(self, other) :
        return tuple(self) == tuple(other)

    def __hash__(self) :
        hashes = map(hash, self._components)
        return functools.reduce(operator.xor, hashes, 0)

    def __abs__(self) :
        return math.sqrt(sum(x*x for x in self))

    def __bool__(self) :
        return bool(abs(self))


    def __len__(self) :
        return len(self._components)

    def __getitem__(self, index) :
        cls = type(self)

        if isinstance(index, slice) :
            return cls(self._components[index])
        elif isinstance(index, numbers.Integral) :
            return self._components[index]
        else :
            raise TypeError(f"{cls.__name__} indices must be integers")


    def __bytes__(self) :
        return (bytes([ord(self.typecode)]) +
                bytes(self._components))

    @classmethod
    def frombytes(cls, octets):
        typecode = chr(octets[0])
        print (typecode)
        memv = memoryview(octets[1:]).cast(typecode)
        return cls(memv)




   
        
