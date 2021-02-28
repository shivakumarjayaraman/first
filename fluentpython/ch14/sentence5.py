#!/usr/bin/env python

## generator expression

import re
import reprlib

class Sentence :
    RE_WORD = re.compile("\w+")

    def __init__(self, text) :
        self._text = text

    def __repr__(self) :
        return f"Sentence({reprlib.repr(self._text)})"

    def __iter__(self) :
        return (match.group() for match in Sentence.RE_WORD.finditer(self._text))
