#!/usr/bin/env python

## RETURN A GENERATOR FUNCTION (function that has a yield in it)
import re
import reprlib

class Sentence:
    RE_WORD = re.compile("\w+")

    def __init__(self, text) :
        self._text = text
        self._words = Sentence.RE_WORD.findall(text)

    def __repr__(self) :
        return f"Sentence({reprlib.repr(self._text)})"

    ## a func that has a yield in it, returns a gen-func when it is called (which honors iter semantics)
    def __iter__(self) :
        for w in self._words :
            yield w

