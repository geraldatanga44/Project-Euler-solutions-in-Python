"""
2520 is the smallest number that can be divided by each of the numbers
from 1 to 10 without any remainder.What is the smallest positive number
that is evenly divisible by all of the numbers from 1 to 20?
"""


def circuit(n):
    div = [x for x in range(11, 21)]  # divisors
    for i in div:
        if n % i != 0:
            return False  # discard if any fails
    return True


def smallest():
    denom = 2520  # base case for 1- 10
    while not circuit(denom):
        denom += 2520  # 10 is factor of 20 increment by base case
    return denom


print(smallest())
