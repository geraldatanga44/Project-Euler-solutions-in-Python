"""
Each new term in the Fibonacci sequence is generated by
adding the previous two terms. By starting with 1 and 2,
the first 10 terms will be:1, 2, 3, 5, 8, 13, 21, 34, 55, 89, ...
By considering the terms in the Fibonacci sequence
whose values do not exceed four million, find the
sum of the even-valued terms.
"""


def evenfib(lim):
    seq = [1, 2]  # initial sequence values
    index = 0  # used to calculate next sequence
    while seq[index] < lim:  # generate sequence less than sequence
        seq.append(seq[index] + seq[index + 1])  # calculate next sequence
        index += 1  # increment index
    even = [x for x in seq if x % 2 == 0]  # return list of even fib
    return sum(even)  # return sum of even fib numbers


print(evenfib(4000_000))
