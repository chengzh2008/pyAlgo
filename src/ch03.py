"""Ch03"""

def is_prime(n):
    """check if n is a prime"""

    for i in range(2, n):
        if n % i == 0:
            return False
    return True

def rec_sum(seq, i=0):
    if i == len(seq):
        return 0
    return rec_sum(seq, i + 1) + seq[i]

def rec_cost_sum(seq, i=0):
    if i == len(seq):
        return 1
    return rec_cost_sum(seq, i + 1) + 1

def merge_sort(seq):
    """Simple mergesort implementation"""

    mid = len(seq)//2
    lft, rgt = seq[:mid], seq[mid:]
    if len(lft) > 1:
        lft = merge_sort(lft)
    if len(rgt) > 1:
        rgt = merge_sort(rgt)
    res = []
    while lft and rgt:
        if lft[-1] > rgt[-1]:
            res.append(lft.pop())
        else:
            res.append(rgt.pop())
    res.reverse()
    return (lft or rgt) + res
