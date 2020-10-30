#!/usr/bin/env python

class Simple :

    serial = 1

    @classmethod
    def getNextSerial(cls) :
        val = cls.serial
        cls.serial += 1
        return val

    def __init__(self) :
        self.s = Simple.getNextSerial()



