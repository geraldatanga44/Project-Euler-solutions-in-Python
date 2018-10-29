def circuit(n):
    div = [x for x in range(11, 21)]
    for i in div:
        if n % i != 0:
            return False
    return True


def smallest():
    denom = 2520
    while not circuit(denom):
        denom += 2520
    return denom


print(smallest())
