"""
A Pythagorean triplet is a set of three natural numbers,
a < b < c, for which, a^2 + b^2 = c^2
For example, 3^2 + 4^2 = 9 + 16 = 25 = 5^2.
There exists exactly one Pythagorean triplet for
which a + b + c = 1000.Find the product abc.
"""

import math


def pythagorean(a, b):  # accept side a and b
    ab = math.pow(a, 2) + math.pow(b, 2)  # square and add values
    return math.sqrt(ab)  # calculate hypotenuse


def triplet(lim):
    prod = 0
    for a in range(3, lim):  # start with 3
        for b in range(a + 1, lim):  # next value is 4 == 3 + 1
            c = pythagorean(a, b)
            if (a + b + c) == lim:  # check a, b, c == limit
                prod = int(a * b * c)  # assign product
    return prod  # return product


print(triplet(1000))
