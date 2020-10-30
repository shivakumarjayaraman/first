#!/usr/bin/env python

from hypothesis import given
import hypothesis.strategies as some

@given(some.lists(some.integers()))
def test_list_size_across_sorting(a_list) :
    f = open("opfile", "a+")
    sz = len(a_list)
    f.write("-----------------\n")
    f.write(str(a_list))
    a_list.sort()
    sz2 = len(a_list)
    assert(sz == sz2)
    for i in range(20):
        f.write(f"Len is {sz2}")
    f.close()

