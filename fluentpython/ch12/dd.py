class DoppelDict(dict) :
    def __setitem__(self, key, val) :
        super().__setitem__(key, [val]*2)


