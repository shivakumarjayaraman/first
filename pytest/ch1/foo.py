#!/usr/bin/env python

from collections import namedtuple

Task = namedtuple("Task", ['summary', 'owner', 'done', 'id'])
Task.__new__.__defaults__ = (None, None, False, None)

t = Task('learning pytest', 'shiva', True, 23)

print (t.summary)
