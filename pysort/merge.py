
def sort(a):
    if len(a) <= 1:
        return a
    mid = int(len(a) / 2)
    l = a[:mid]
    r = a[mid:]
    l = sort(l)
    r = sort(r)
    return merge(l, r)

def merge(l, r):
    i, j = 0, 0
    res = []
    while i < len(l) or j < len(r):
        if i < len(l) and j < len(r):
            if l[i] < r[j]:
                res.append(l[i])
                i += 1
            else:
                res.append(r[j])
                j += 1
        elif i < len(l):
            res.append(l[i])
            i += 1
        elif j < len(r):
            res.append(r[j])
            j += 1
    return res
