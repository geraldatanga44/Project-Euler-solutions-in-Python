"""
The sum of the squares of the first ten natural numbers is,
1^2 + 2^2 + ... + 10^2 = 385
The square of the sum of the first ten natural numbers is,
(1 + 2 + ... + 10) = 55^2 = 3025

Hence the difference between the sum of the squares of
the first ten natural numbers and the square of the sum is 3025 − 385 = 2640.

Find the difference between the sum of the squares of the
first one hundred natural numbers and the square of the sum.
"""
import math


def sumsquare(lim):
    return sum([int(math.pow(x, 2)) for x in range(11, lim + 1)]) + 385  # add base 1-10


def sqaresum(lim):
    return int(math.pow(sum([j for j in range(1, lim + 1)]), 2))  # square then sum


def difference(lim):
    return sqaresum(lim) - sumsquare(lim)  # get difference


print(difference(100))  # print results
