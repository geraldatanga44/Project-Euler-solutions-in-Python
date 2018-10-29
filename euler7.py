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
