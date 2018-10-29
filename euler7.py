import library.helpers


def tenthousandoneprime(lim):
    counter = 1
    number = 3
    while counter < lim:
        if library.helpers.isprime(number):
            counter += 1
        if counter == lim:
            break
        number += 2
    return number


def tenthousandoneprime0(lim):
    primes = []  # track number of primes
    val = 3  # skip 2 as the only even prime
    while len(primes) < lim:
        if library.helpers.isprime(val):
            primes.append(val)
        val += 2
    return primes[len(primes) - 2]


print(tenthousandoneprime0(10001))
