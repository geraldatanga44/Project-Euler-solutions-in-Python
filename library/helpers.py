import math


def isprime(n):
    if n < 2:  # first prime is 2
        return False
    divset = set()  # remove duplicates
    sqrt = int(math.sqrt(n)) + 1  # lower bound factors
    for i in range(1, sqrt):
        if n % i == 0:
            divset.add(i)  # add found factor
        if len(divset) > 1:  # limit prime search to two factors
            return False
    return True


def factors(n):
    divset = set()  # remove duplicates
    sqrt = int(math.sqrt(n)) + 1  # lower bound factors
    for i in range(1, sqrt):
        if n % i == 0:
            divset.add(i)  # use lower bound divisors
            divset.add(n // i)  # find upper bound divisors
    return divset
