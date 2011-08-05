#!/usr/bin/python
from __future__ import division
from itertools import count, takewhile, starmap

"""
Three distinct points are plotted at random on a Cartesian plane, for which 
-1000 <= x, y <= 1000, such that a triangle is formed.

Consider the following two triangles:

A(-340,495), B(-153,-910), C(835,-947)

X(-175,41), Y(-421,-714), Z(574,-645)

It can be verified that triangle ABC contains the origin, whereas triangle XYZ 
does not.

Using triangles.txt (right click and 'Save Link/Target As...'), a 27K text file 
containing the co-ordinates of one thousand "random" triangles, find the number 
of triangles for which the interior contains the origin.
"""

Q1 = 1
Q2 = 2
Q3 = 3
Q4 = 4

quadrants = set([Q1, Q2, Q3, Q4])

# The quadrants depending on the signs of x and y are as follows:
# Q1: x > 0, y > 0 
# Q2: x < 0, y > 0
# Q3: x < 0, y < 0
# Q4: x > 0, y < 0
quadrant = lambda x, y: (x > 0 and y > 0 and Q1) or \
                        (x < 0 and y > 0 and Q2) or \
                        (x < 0 and y < 0 and Q3) or \
                        (x > 0 and y < 0 and Q4)

# Given a line and a range (so a line segment), determine which quadrants the 
# line passes through.
#
# The function below does this by moving x=x1 to x2 in increments of epsilon, 
# and taking the current quadrant that the point (x, f(x)) lies in. 
def quadrants_touched(f, x1, x2, epsilon=7/8):
    return (x1 > x2 and quadrants_touched(f, x2, x1, epsilon)) or \
           set(filter(None, map(lambda x: quadrant(x, f(x)), \
               takewhile(lambda x: x <= x2, count(x1, epsilon)))))

# Does the triangle represented by (x1, y1), (x2, y2), (x3, y3) contain (0, 0)?
def contains_origin(x1, y1, x2, y2, x3, y3):
    if 0 in [x1 - x2, x2 - x3, x3 - x1]: # Ensure no div. by zero below.
        return False

    # From a pair of points, get the y-intercept of the line between them.        
    intercept = lambda x1_, y1_, x2_, y2_: ((y1_ - y2_)/(x1_ - x2_))*x1_ - y1_

    # Functions of x representing a line between points 1 & 2, 2 & 3, and 3 & 1.
    line12 = lambda x: ((y1 - y2)/(x1 - x2)) * x - intercept(x1, y1, x2, y2)
    line23 = lambda x: ((y3 - y2)/(x3 - x2)) * x - intercept(x2, y2, x3, y3)
    line31 = lambda x: ((y3 - y1)/(x3 - x1)) * x - intercept(x1, y1, x3, y3)

    # Determine which quadrants each line segment lie in and take a union of
    # the resulting set of quadrants.
    quads = quadrants_touched(line12, x1, x2) | \
            quadrants_touched(line23, x2, x3) | \
            quadrants_touched(line31, x1, x3)

    # If a triangle contains the origin, the 3 lines representing it will touch 
    # each quadrant.
    return quadrants == quads

if __name__ == '__main__':
    # Open the file, read its lines, strip out \r and \n chars, and convert 
    # each string into an integer.
    triangles = map(lambda s: map(int, s.rstrip().split(",")), \
                    open('triangles.txt').readlines())

    # Make a list of those triangles which contain the origin, and take the
    # length of that list; the answer.
    print len(filter(lambda t: contains_origin(*t), triangles))


