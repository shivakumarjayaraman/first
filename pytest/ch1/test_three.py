from foo import *

def test_foo():
    t = Task('a', 'shiva', True, 12)
    assert t == ('a', 'shiva', True, 12)

def test_defaults() :
    t1 = Task()
    t2 = Task(None, None, False, None)

    assert t1 == t2

def test_member_access():
    t = Task('buy milk', 'brian')
    assert t.summary == 'buy milk'
    assert t.owner == 'brian'
    assert (t.done, t.id) == (False, None)

def test_asdict():
    t_task = Task('do something', 'okken', True, 21)
    t_dict = t_task._asdict()
    expected = {'summary' : 'do something', 
                 'done' : True,
                 'owner' : 'okken',
                 'id' : 21}
    assert t_dict == expected

def test_replace():
    t_before = Task('finish book', 'brian', False)
    t_after = t_before._replace(id=10, done=True)
    t_expected = Task('finish book', 'brian', True, 10)
    assert t_after == t_expected
