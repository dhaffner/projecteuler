#!/usr/bin/python
from itertools import ifilter, imap, permutations, count
from itertools import combinations, chain, dropwhile, takewhile
from helpers import *
from operator import add

# for 101
from numpy import polyfit, polyval

def problem49():
    """
    The arithmetic sequence, 1487, 4817, 8147, in which each of the terms increases 
    by 3330, is unusual in two ways: (i) each of the three terms are prime, and, 
    (ii) each of the 4-digit numbers are permutations of one another.

    There are no arithmetic sequences made up of three 1-, 2-, or 3-digit primes, 
    exhibiting this property, but there is one other 4-digit increasing sequence.

    What 12-digit number do you form by concatenating the three terms in this 
    sequence?
    """
    # Return an iterable of the numbers formed by permuting digits of n.
    permute = lambda n: imap(lambda p: int(''.join(p)), permutations(str(n)))

    # Filter all non-4-digit numbers and composites
    numberfilter = lambda n: 1000 <= n <= 10000 and isprime(n)
    
    # From each collection of numbers containing the same digits, take those
    # 3-tuples which represent arithmetic sequences.
    samediff = lambda lst: filter(lambda (a, b, c): abs(a-b) == abs(b-c) and \
                                  a != b and a != c, combinations(lst, r=3))

    # For some reason I want to write this in a functional way.
    # I'll comment it later.
    return dropwhile(lambda s: s == '148748178147', \
      map(lambda tup: reduce(add, sorted(map(str, tup))), \
      flatten(ifilter(None, map(samediff, \
      imap(lambda prime: ifilter(numberfilter, permute(prime)), \
      ifilter(isprime, xrange(1000, 10000)))))))).next()

def problem101():
    """
    Consider the following tenth degree polynomial generating function:

    u_n = 1 - n + n^2 - n^3 + n^4 - n^5 + n^6 - n^7 + n^8 - n^9 + n^10

    Find the sum of FITs for the BOPs.
    """
    # General algorthim:
    #
    # The given function u is 10th-order, so assume no BOPs exist at OP(11, -).
    # For 1 <= k <= 10, calculate OP(k, n) for a general n, and get the first 
    # term in sequence OP(k, 1), OP(k, 2), ..., where that term disagrees with 
    # u(n). Compute a vector of these such values whose sum should be the 
    # answer.
    u = lambda n: (n-1)*n*(n**4+n**3+n**2+n+1)*((n-1)*n*(n**2+1)+1)+1 # factored
    OP = lambda k, n: polyval(polyfit(range(1, k + 1), 
                              map(u, xrange(1, k + 1)), k - 1), n)

    return reduce(lambda s, (k, uk, tk): s + tk, 
                  filter(lambda (k, uk, tk): not approx_equal(uk, tk), 
                         map(lambda k: (k, u(k + 1), OP(k, k + 1)), 
                             xrange(1, 11))), 0)

def problem38():
    ceiling = 987654321
    digits = set(range(1, 10))
    def is_pandigital(n):
        return set(map(int, str(n))) == digits

    def concat_prod(k, n):
        return int(reduce(add, (str(k*i) for i in xrange(1, n+1))))

    def form_num(k):
        return ifilter(is_pandigital, takewhile(lambda i: i <= ceiling, (concat_prod(k, n) for n in count(2))))

    return max(flatten(form_num(k) for k in xrange(192, 100000)))




