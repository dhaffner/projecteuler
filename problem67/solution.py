#!/usr/bin/python

"""
Find the maximum total from top to bottom in triangle.txt, a 15K text file
containing a triangle with one-hundred rows.
"""

def run(input='triangle.txt'):
	lines = map(lambda s: s.rstrip().split(' '), open(input).readlines())

	triangle = lambda i, j: int(lines[i][j])
	# i = row, j = column
	# From (i, j) in the triangle, you can "move" to (i+1, j) or (i+1, j+1),
	# So if maxpath(i, j) is the max path starting at position (i, j), then
	# maxpath(i, j) = triangle[i, j] + max(maxpath(i+1, j), maxpath(i+1, j+1))
	C = dict()
	def maxpath(i, j):
		if (i, j) in C:
			return C[(i, j)]
		elif i >= len(lines) or j >= len(lines):
			return 0
		else:
			C[(i, j)] = triangle(i, j) + max(maxpath(i + 1, j), \
                                             maxpath(i + 1, j + 1))
		return C[(i, j)]

	print maxpath(0, 0)

if __name__ == '__main__':
	run()