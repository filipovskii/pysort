def sort(seq):
    """"Bubble sort implementation"""
    l = len(seq)
    swap_used = True
    while swap_used:
        swap_used = False
        for i in range(1, l):
            if seq[i] < seq[i - 1]:
                seq[i], seq[i - 1] = seq[i - 1], seq[i]
                swap_used = True
