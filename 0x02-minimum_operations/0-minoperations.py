#!/usr/bin/python3
"""
Minimum Operation module for calculating minimum operation
"""


def minOperations(n: int) -> int:
    """
    Returns a dictionary representing the prime factorization of a number.
    The keys of the dictionary are the prime factors, and the values are
    the corresponding exponents.
    """
    if not isinstance(n, int):
        return 0

    factors = []
    for i in range(1, n):
        if n % i == 0:
            factors.append(i)

    copy = 0
    paste = 0
    clipb = ''
    list_h = 'H'

    while len(list_h) < n:
        if len(list_h) in factors:
            copy += 1
            clipb = list_h

        paste = paste + 1
        list_h = list_h + clipb

    operations = copy + paste
    return operations
