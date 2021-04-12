#!/bin/python3

import os
import sys

#
# Complete the waiter function below.


def primeNumbers(n):
    prime = []
    i = 2
    while(len(prime) < n):
        isPrime = True
        for x in range(2, i//2+1):
            if i % x == 0:
                isPrime = False
                break
        if isPrime:
            prime.append(i)
        i += 1
    return(prime)


def waiter(stacks, q):
    pn = primeNumbers(q)
    b = []
    for iLoop in range(0, q):
        if iLoop >= 0:
            stacks = stacks[::-1]
        bi = []
        for idx in range(len(stacks)-1, -1, -1):
            val = stacks[idx]
            if val % pn[iLoop] == 0:
                bi.append(val)
                stacks.pop(idx)
        b.extend(bi)
    return(b + stacks[::-1])


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    nq = input().split()

    n = int(nq[0])

    q = int(nq[1])

    number = list(map(int, input().rstrip().split()))

    result = waiter(number, q)

    fptr.write('\n'.join(map(str, result)))
    fptr.write('\n')

    fptr.close()
