#!/usr/bin/env python

## Lazy generator

import re
import reprlib

class Sentence :
    RE_WORD = re.compile("\w+")

    def __init__(self, text) :
        self._text = text

    def __repr__(self) :
        return f"Sentence({reprlib.repr(self._text)})"

    def __iter__(self) :
        ## RE_WORD.finditer .. returns a gen
        for match in Sentence.RE_WORD.finditer(self._text) :
            yield match.group()
