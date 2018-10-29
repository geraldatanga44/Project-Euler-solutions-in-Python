"""
A palindromic number reads the same both ways. The largest palindrome made
from the product of two 2-digit numbers is 9009 = 91 × 99.
Find the largest palindrome made from the product of two 3-digit numbers.
"""


def reverse(n):  # reverse number mathematically
    result = 0
    while n != 0:
        remainder = n % 10  # get last digit
        result = (result * 10) + remainder  # find proper place
        n //= 10  # reduce number by 10 place
    return result  # return reversed number


def product(lim):
    prod = 0
    for i in range(99, lim, 6):  # use base case to start loop
        for j in range(99, lim, 2):
            mul = j * i  # generate all combinations
            if mul == reverse(mul):
                prod = max(prod, mul)  # largest palindrome product
    return prod  # return largest palindrome product


print(product(1000))
