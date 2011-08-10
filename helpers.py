#!/usr/binpython
from itertools import chain, count, ifilter
from random import randint

# Miller-Rabin primality test.
# Lifted directly from http://www.ics.uci.edu/~eppstein/numth/egypt/egypt.py
def millrab(n, max=30):
    """
    Miller-Rabin primality test as per the following source:
    http://www.wikipedia.org/wiki/Miller-Rabin_primality_test
    Returns probability p is prime: either p = 0 or ~1,
    """
    if not n%2: return n == 2
    k = 0
    z = n - 1

    # compute m,k such that (2**k)*m = n-1
    while not z % 2:
      k += 1
      z //= 2
    m = z

    # try tests with max random integers between 2,n-1
    ok = 1
    trials = 0
    p = 1
    while trials < max and ok:
        a = randint(2,n-1)
        trials += 1
        test = pow(a,m,n)
        if (not test == 1) and not (test == n-1):
            # if 1st test fails, fall through
            ok = 0
            for r in range(1,k):
                test = pow(a, (2**r)*m, n)
                if test == (n-1):
                    ok = 1 # 2nd test ok
                    break
        else: ok = 1  # 1st test ok
        if ok==1:  p *= 0.25
            
    if ok:  return 1 - p
    else:   return 0


def primes(start=2):
    return ifilter(isprime, count(start))

def isprime(n):
	return millrab(n) > 0

def flatten(lst):
    return chain.from_iterable(lst)

def approx_equal(a, b, epsilon=1e-3):
    return abs(a-b) <= epsilon

