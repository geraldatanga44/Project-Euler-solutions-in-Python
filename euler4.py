def reverse(n):
    result = 0
    while n != 0:
        remainder = n % 10
        result = (result * 10) + remainder
        n //= 10
    return result


def product(lim):
    prod = 0
    for i in range(99, lim, 6):
        for j in range(99, lim, 2):
            mul = j * i
            if mul == reverse(mul):
                prod = max(prod, mul)
    return prod


print(product(1000))
