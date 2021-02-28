#!/usr/bin/env python

## A classic GoF iterator

import re
import reprlib

class Sentence :
    RE_WORD = re.compile("\w+")

    def __init__(self, text) :
        self._text = text
        self._words = Sentence.RE_WORD.findall(text)

    def __iter__(self) :
        return SentenceIterator(self._words)


class SentenceIterator :
    def __init__(self, words):
        ## need to keep state which is why we cant just have Sentence be both an iterable and a iterator
        self._index = 0  
        self._words = words

    def __iter__(self) : return self

    def __next__(self) :
        if (self._index == len(self._words)) :
            raise StopIteration()
        word = self._words[self._index]
        self._index += 1
        return word

