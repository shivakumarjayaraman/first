#!/usr/bin/env python

import collections

Card = collections.namedtuple('Card', ['rank', 'suit'])

class FrenchDeck2(collections.MutableSequence):
    ranks = [str(n) for n in range(2, 11)] + list('JQKA')
    suits = 'spades diamonds clubs hearts'.split()

    def __init__(self) :
        self._cards = [Card(r, s) for s in FrenchDeck2.suits for r in FrenchDeck2.ranks]

    def __len__(self) :
        return len(self._cards)

    def __getitem__(self, pos) :
        return self._cards[pos]

    def __setitem__(self, pos, item) : 
        self._cards[pos] = item

    def __delitem__(self, pos) :
        del self._cards[pos]

    def insert(self, pos, item) :
        self._cards.insert(pos, item)
