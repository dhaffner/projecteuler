#!/usr/bin/python

"""
Using network.txt (right click and 'Save Link/Target As...'), a 6K text file
containing a network with forty vertices, and given in matrix form, find the
maximum saving which can be achieved by removing redundant edges whilst
ensuring that the network remains connected.
"""

from operator import add
from itertools import product, starmap
from heapq import heapify, heappop

DOT = "network.dot"

def run(input='network.txt'):
    lines = map(lambda s: s.rstrip().split(','), \
                open(input).readlines())

    def weight(i, j):
        t = lines[i][j]
        w = t != '-' and int(t) or 0
        return w

    # Represent the vertices with integers 0-39
    V = range(len(lines))

    # The "i > j" condition keeps us from using duplicate edges and the
    # "weight(i, j) > 0" lets us use only edges that exist in the graph.
    # (The weight function above returns 0 for "-" entries in the file.)
    E = filter(lambda (i, j): i > j and weight(i, j) > 0, product(V, V))

    # Run Kruskal's algorthim to find an minimum spanning tree.
    # Define an elementary cluster C(v) <- {v}
    C = dict((v, set([v])) for v in V)

    # Initialize a priority queue Q to contain all edges in G, using the
    # weights as keys.
    Q = map(lambda (u, v): (weight(u, v), u, v), E)
    heapify(Q)

    # Define a tree T <- {}
    # T will ultimately contain the edges of the MST
    T = set()

    # n is the total number of vertices
    n = len(V)

    while len(T) < n-1:
        # Edge (u, v) is the minimum weighted route from u to v
        w, u, v = heappop(Q)

        # Prevent cycles in T. add (u, v) only if T does not already contain
        # a path between u and v.
        if C[v] != C[u]:
            # Add edge (u, v) to T.
            T.add((u, v))
            # Merge C[u] and C[v]/
            C[u].update(C[v])
            for x in C[u]:
                C[x] = C[u]

    # T now describes a miniumum spanning tree on G.
    # Produce a DOT language file to visualize T.
    dot(reduce(add, T), T, weight)

    # Print the savings, as to answer problem #107.
    Tweight = sum(starmap(weight, T))
    Gweight = sum(starmap(weight, E))
    print Gweight - Tweight

def dot(V, E, weight):
    f = open(DOT, "w+")
    f.write('graph G {\n')
    f.write('    node[fontname=Verdana,fontsize=10];\n')
    f.write('    edge[fontname=Verdana,fontsize=9,fontcolor="#44687e"];\n')

    for v in V:
        f.write("    %2s [label=%s];\n" % (v, v))
    for (u, v) in E:
        f.write("    %2s -- %2s [label=%s];\n" % (u, v, weight(u, v)))

    f.write('}\n\n')
    f.close()

if __name__ == '__main__':
    import sys
    if len(sys.argv) > 1:
        run(sys.argv[1])
    else:
        run()