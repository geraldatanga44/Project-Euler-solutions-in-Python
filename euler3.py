import library.helpers


def findprime(n):
    if n < 2:  # first prime is 2
        return 0
    primes = [x for x in library.helpers.factors(n) if library.helpers.isprime(x)]  # list of all prime divisors
    return max(primes)  # return max prime divisor


print(findprime(600851475143))
