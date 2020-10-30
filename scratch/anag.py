#!/usr/bin/env python
import itertools
import macdict

def anag(word, n) :
    letters = [l for l in word]
    subsets = itertools.combinations(letters, n)
    nletterwords = ("".join(p) for s in subsets for p in itertools.permutations(s))
    goodwords = [w  for w in nletterwords if macdict.lookup_word(w)]
    return set(goodwords)
    

print (anag("sumitkar", 5))
