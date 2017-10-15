"""utility functions"""
from functools import wraps


def memo(fn):
    """convert fn to a memoization one
    run in the iPython
    fib = memo(fib)
    fib(100) returns 573147844013817084101L quickly
    """
    cache = {}
    @wraps(fn)
    def wrap(*args):
        if args not in cache:
            cache[args] = fn(*args)
        return cache[args]
    return wrap
