#!/usr/bin/env python

import collections

Card = collections.namedtuple('Card', ['rank', 'suit'])

class FrenchDeck :
    ranks = [str(n) for n in range(2, 11)] + list("JQKA")
    suits = "spades diamonds clubs hearts".split()

    def __init__(self) :
        self.cards = [Card(r, s) for r in self.ranks for s in self.suits]

    def __len__(self) : 
        return len(self.cards)

    def __getitem__(self, pos) :
        return self.cards[pos]


suit_values = dict(spades=3, hearts=2, diamonds=1, clubs=0)
def spades_high(card) :
    rank_val = FrenchDeck.ranks.index(card.rank)
    return rank_val * len(FrenchDeck.suits) + suit_values[card.suit]


if __name__ == "__main__" :
    print ("Yes")
