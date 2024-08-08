#!/usr/bin/python3

""" Module that contains a method that calculates
the fewest number of operations needed
to result in exactly n H characters in the file.
"""


def minOperations(n):
    """calculates the fewest number of operations
    needed to result in exactly n H characters
    """
    str = 'H'  # Character to be formed
    opers = 0  # Number of operations needed
    factor = 2  # Starting factor

    if n < 0:
        return 0

    while n > 1:
        while n % factor == 0:
            opers += factor
            n //= factor  # Divide n by factor

        factor += 1  # Increment factor

    return opers
