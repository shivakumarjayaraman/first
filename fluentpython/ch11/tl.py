from random import randrange
from tombola import *

@Tombola.register
class TomboList(list) :
    def pick(self) :
        try :
            return self.pop(randrange(len(self)))
        except :
            raise LookupError('pop from TomboList')

    load = list.extend

    def loaded(self) :
        return bool(self)

    def inspect(self) :
        return tuple(sorted(self))
