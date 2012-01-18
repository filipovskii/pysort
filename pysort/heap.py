from math import floor

def max_heapify(a, i):
    """ Make max heap from binary tree, 
    that already is a max heap except for root element.
    """
    len_ = len(a)
    l = left(i)
    r = right(i)

    largest = i
    if l < len_ and a[l] > a[largest]:
        largest = l
    if r < len_ and a[r] > a[largest]:
        largest = r
    if largest != i:
        a[i], a[largest] = a[largest], a[i]
        max_heapify(a, largest)

def build_max_heap(a):
    """ Build max heap from array """
    for i in range(floor(len(a) / 2), -1, -1):
        max_heapify(a, i)

def left(i):
    """ Determine index of left node"""
    return 2 * i + 1

def right(i):
    """ Determine index of right node"""
    return 2 * i + 2

def sort(a):
    build_max_heap(a)
    b = []
    n = len(a) - 1
    for i in range(n, -1, -1):
        b.insert(0, a[0])
        a[0] = a[i]
        del(a[i])
        max_heapify(a, 0)
    return b
