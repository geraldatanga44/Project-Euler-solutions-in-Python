"""
By listing the first six prime numbers: 2, 3, 5, 7, 11,
and 13, we can see that the 6th prime is 13.
What is the 10 001st prime number?
"""
import library.helpers


def tenthousandoneprime0(lim):
    primes = []  # track number of primes
    val = 3  # skip 2 as the only even prime
    while len(primes) < lim:
        if library.helpers.isprime(val):
            primes.append(val)
        val += 2
    return primes[len(primes) - 1]  # We didn't include 2 so lim = 100000


print(tenthousandoneprime0(10000))
