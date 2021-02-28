from tombola import Tombola
import random

class BingoCage(Tombola):
    def __init__(self, items) :
        self._randomizer = random.SystemRandom()
        self._items = []
        self.load(items)

    def load(self, items) :
        self._items.extend(items)
        self._randomizer.shuffle(self._items)

    def pick(self) :
        try :
            return self._items.pop()
        except IndexError :
            raise LookupError('Cage empty')

    def __call__(self) :
        return self.pick()


