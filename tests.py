from __init__ import *


def test_min_basic():
    mn = MinHeap()
    mn.push("a", 1)

    assert mn.__repr__()
    assert not mn.empty
    assert len(mn) == 1
    assert mn.peak() == 'a'
    assert mn.pop() == 'a'


def test_min_sort():
    mn = MinHeap()
    foo1 = [1, 4, 2, 6, 3]
    foo2 = []

    for item in foo1:
        mn.push(item)
    for _ in foo1:
        foo2.append(mn.pop())

    foo1.sort()
    assert foo2 == foo1


def test_max_basic():
    mx = MaxHeap()
    assert mx.empty
    assert len(mx) == 0

    mx.push("a", 1)

    assert mx.__repr__()
    assert not mx.empty
    assert len(mx) == 1
    assert mx.peak() == 'a'
    assert mx.pop() == 'a'


def test_max_sort():
    mx = MaxHeap()
    foo1 = [1, 4, 2, 6, 3]
    foo2 = []

    for item in foo1:
        mx.push(item)
    for _ in foo1:
        foo2.append(mx.pop())

    foo1.sort(reverse=True)
    assert foo2 == foo1


# the lazy man's unit testing framework
if __name__ == "__main__":
    test_min_basic()
    test_min_sort()
    test_max_basic()
    test_max_sort()
