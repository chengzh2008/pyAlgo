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
