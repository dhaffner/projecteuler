#!/usr/bin/python

"""
Find the maximum total from top to bottom of the triangle below:
"""

triangle = \
	[[75],
	 [95, 64],
	 [17, 47, 82],
	 [18, 35, 87, 10],
	 [20,  4, 82, 47, 65],
	 [19,  1, 23, 75,  3, 34],
	 [88,  2, 77, 73,  7, 63, 67],
	 [99, 65,  4, 28,  6, 16, 70, 92],
	 [41, 41, 26, 56, 83, 40, 80, 70, 33],
	 [41, 48, 72, 33, 47, 32, 37, 16, 94, 29],
	 [53, 71, 44, 65, 25, 43, 91, 52, 97, 51, 14],
	 [70, 11, 33, 28, 77, 73, 17, 78, 39, 68, 17, 57],
	 [91, 71, 52, 38, 17, 14, 91, 43, 58, 50, 27, 29, 48],
	 [63, 66,  4, 68, 89, 53, 67, 30, 73, 16, 69, 87, 40, 31],
	 [04, 62, 98, 27, 23,  9, 70, 98, 73, 93, 38, 53, 60,  4, 23]]

def run():
	# i = row, j = column.
	# From (i, j) in the triangle, you can "move" to (i+1, j) or (i+1, j+1).
	# So if maxpath(i, j) is the max path starting at position (i, j), then
	# maxpath(i, j) = triangle[i, j] + max(maxpath(i+1, j), maxpath(i+1, j+1))
	def maxpath(i, j):
		if i >= len(triangle) or j >= len(triangle):
			return 0
		else:
			return triangle[i][j] + max(maxpath(i+1, j), maxpath(i+1, j+1))

	print maxpath(0, 0)

if __name__ == '__main__':
	run()