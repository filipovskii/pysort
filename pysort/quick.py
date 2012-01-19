from random import randint

def partition(a, frm, to):
    pivot = randint(frm, to)
    new_pivot = pivot
    last_small = frm - 1
    last_big = frm
    for i in range(frm, to + 1):
        if a[i] > a[pivot]:
            last_big += 1
        else:
            last_small += 1
            a[last_small], a[i] = a[i], a[last_small]
            if i == pivot:
                new_pivot = last_small
    a[new_pivot], a[last_small] = a[last_small], a[new_pivot]
    print("a paritioned: {0}, pivot: a[{1}] = {2}"
            .format(a[frm: to + 1], last_small, a[last_small]))
    return last_small # new pivot position

def sort(a, frm = 0, to = None):
    if to == None:
        to = len(a) - 1
    if to - frm < 1:
        return a
    pivot = partition(a, frm, to)
    sort(a, frm, pivot - 1)
    sort(a, pivot + 1, to)
    return a
