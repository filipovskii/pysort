def sort(seq):
    """Insertion sort algorithm implementation"""
    print(seq)
    for i in range(1, len(seq)):
        el = seq[i]
        i_pos = i
        for j in range(i - 1, -1, -1):
            print("j =", j)
            if el < seq[j]:
                print("{0} < {1}. swap".format(el, seq[j]))
                del seq[i_pos]
                seq.insert(j, el)
                i_pos = j
            else:
                print("{0} > {1}".format(seq[i], seq[j]))
            print(seq)
