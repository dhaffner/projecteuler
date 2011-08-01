#!/usr/bin/python
"""
The arithmetic sequence, 1487, 4817, 8147, in which each of the terms increases 
by 3330, is unusual in two ways: (i) each of the three terms are prime, and, 
(ii) each of the 4-digit numbers are permutations of one another.

There are no arithmetic sequences made up of three 1-, 2-, or 3-digit primes, 
exhibiting this property, but there is one other 4-digit increasing sequence.

What 12-digit number do you form by concatenating the three terms in this sequence?
"""
from itertools import ifilter, imap, permutations
from itertools import combinations, chain, dropwhile

from helpers import isprime
from operator import add

def problem49():
    # Flatten one level of nesting
    flatten = lambda lst: chain.from_iterable(lst)
    
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

print problem49()
