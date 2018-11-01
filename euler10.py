"""
The sum of the primes below 10 is 2 + 3 + 5 + 7 = 17.
Find the sum of all the primes below two million.
"""

import library.helpers


def primesum(lim):
    result = 5  # only even prime 2 + first odd prime 3
    for n in range(3, lim, 2):  # only go through odd numbers
        if n % 3 == 0:
            continue
        if library.helpers.isprime(n):  # check if prime
            result += n  # add number to result
    return result  # return result


print(primesum(2000_000))
