
def partition(a, frm, to):
    pivot = to
    last_small = frm - 1
    last_big = frm
    for i in range(frm, to + 1):
        if a[i] > a[pivot]:
            last_big += 1
        else:
            last_small += 1
            a[last_small], a[i] = a[i], a[last_small]
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
