import math


def sumsquare(lim):
    return sum([int(math.pow(x, 2)) for x in range(11, lim + 1)]) + 385


def sqaresum(lim):
    return int(math.pow(sum([j for j in range(1, lim + 1)]), 2))


def difference(lim):
    return sqaresum(lim) - sumsquare(lim)


print(difference(100))
