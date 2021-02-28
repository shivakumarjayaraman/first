import re
import reprlib

RE_WORD = re.compile("\w+")

class Sentence:
    def __init__(self, text) :
        self._text = text
        self._words = RE_WORD.findall(self._text)

    def __getitem__(self, index) :
        return self._words[index]

    def __len__(self) :
        return len(self._words)

    def __repr__(self) :
        return f"Sentence({reprlib.repr(self._text)})"
