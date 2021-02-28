from collections import UserDict

class DoppelDict2(UserDict) :
    def __setitem__(self, key, val) :
        super().__setitem__(key, [val]*2)


class AnswerDict2(UserDict) :
    def __getitem__(self, key) :
        return 42
