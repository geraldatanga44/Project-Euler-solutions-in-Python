"""
If we list all the natural numbers below 10 that are multiples of 3 or 5,
we get 3, 5, 6 and 9. The sum of these multiples is 23.
Find the sum of all the multiples of 3 or 5 below 1000.
"""


def mn(n, m, lim):  # input <n, m, lim>
    sm = min(n, m)  # smallest <n, m>
    xmn = 0  # sum factors of <n or m>
    for x in range(sm, lim):  # loop from <min to lim>
        if x % n == 0 or x % m == 0:  # find a factor of <n or m >
            xmn += x  # reduce factor to xmn
    return xmn  # return xmn


def mn0(n, m, lim):     # input <n, m, lim>
    sm = min(n, m)      # smallest <n, m>
    return sum([x for x in range(sm, lim) if x % n == 0 or x % m == 0])     # sum list of factors


print(mn(3, 5, 1000))
print(mn0(3, 5, 1000))
