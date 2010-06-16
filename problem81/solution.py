#!/usr/bin/python

"""
Find the minimal path sum, in matrix.txt, a 31K text file containing a 80 by 80 
matrix, from the top left to the bottom right by only moving right and down.
"""

def run(input='matrix.txt'):
    lines = map(lambda s: s.rstrip().split(','), \
                open(input).readlines())
    x = y = len(lines) - 1    
    a = lambda i, j: int(lines[j][i])

    C = dict()
    
    def minpathsum(i, j):
        if i < 0 or j < 0:
            return 0
        elif (i, j) in C:
            return C[(i, j)]  

        c = a(i, j)
        
        if j == 0 and i > 0:
            c += minpathsum(i-1, j)
        elif j > 0 and i == 0:
            c += minpathsum(i, j-1)
        else:
            c += min(minpathsum(i-1, j), minpathsum(i, j-1))
            
        C[(i, j)] = c

        return c

    print minpathsum(x, y)
    
if __name__ == '__main__':
    import sys
    if len(sys.argv) > 1:
        run(sys.argv[1])
    else: 
        run()