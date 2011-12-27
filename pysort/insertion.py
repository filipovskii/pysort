import logging

def sort(seq):
    """Insertion sort algorithm implementation"""
    logging.info("Sorting {0}".format(seq))
    for i in range(1, len(seq)):
        j = i - 1
        new_i = i
        while j >= 0 and seq[i] < seq[j]:
            new_i = j
            j = j - 1
        el_i = seq[i]
        del seq[i]
        seq.insert(new_i, el_i)
    logging.info("Sorted. Result: {0}".format(seq))
    return seq
