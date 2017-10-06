"""Ch06 Divide and conquer"""
from collections import defaultdict


def divide_and_conquer(S, divide, combine):
    """General divide and conquer algorithm"""
    if len(S) == 1:
        return S
    L, R = divide(S)
    A = divide_and_conquer(L, divide, combine)
    B = divide_and_conquer(R, divide, combine)
    return combine(A, B)

def bisect_right_1(a, x, lo=0, hi=None):
    """how bisect_right is implementated"""
    if hi is None:
        hi = len(a)
    while lo < hi:
        mid = (lo + hi) // 2
        if x < a[mid]:
            hi = mid
        else:
            lo = mid + 1
    return lo


def partition(seq):
    """partition the seq into two half, pivot is the first item"""
    pi, seq = seq[0], seq[1:]
    lo = [x for x in seq if x <= pi]
    hi = [x for x in seq if x > pi]
    return lo, pi, hi

def partition_in_place(seq, lo=0, hi=None):
    """chose first item as pivot"""
    n = len(seq)

    if hi is None:
        hi = n - 1
    pi = seq[lo]
    left = lo
    right = hi
    while left < right:
        while seq[left] <= pi:
            left += 1
        while seq[right] > pi:
            right -= 1
        if left < right:
            seq[left], seq[right] = seq[right], seq[left]
    seq[lo] = seq[right]
    seq[right] = pi
    return right



def select(seq, k):
    """
    quickselect
    select k smallest items from seq in linear time"""
    lo, pi, hi = partition(seq);
    m = len(lo)
    if m == k:
        return pi
    elif m < k:
        return select(hi, k-m-1)
    else:
        return select(lo, k)

def quick_sort(seq):
    """quicksort"""
    if len(seq) == 1:
        return seq
    lo, pi, hi = partition(seq)
    return quick_sort(lo) + [pi] + quick_sort(hi)

def quick_sort_in_place(seq, lo=0, hi=None):
    """in place quick sort"""
    n = len(seq)
    if hi is None:
        hi = len(seq) - 1
    if lo >= hi:
        return
    p = partition_in_place(seq, lo, hi)
    print "lo: {0}, p: {1}, hi:{1}".format(lo, p, hi)
    quick_sort_in_place(seq, lo, p - 1)
    quick_sort_in_place(seq, p + 1, hi)
