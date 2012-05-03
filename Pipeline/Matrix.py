# This is a class to make matrix math, and storage more managable.
# Written by Murphy Randle, 2012: murphyrandle@gmail.com
# Heavily referenced from: http://www.math.okstate.edu/~ullrich/PyPlug/
# Requires vector class, by same author.
# Only matricies with vectors of equal lengths are functional.
# Anything else will break.
from Vector import Vector


class Matrix(Vector):
    def __init__(self, *indata):
        self.rows = map(Vector, indata)
        self.cols = []

        numCols = len(self.rows[0])
        for i in range(numCols):
            vals = []
            for j in self.rows:
                vals.append(j[i])
            self.cols.append(Vector(vals))

    def __mul__(self, other):
        # This will multiply one matrix by anther.
        # The matricies must have equal rows and columns.
        # Returns a matrix with the result.
        result = []
        for i in [self.rows, self.cols, other.rows, other.cols]:
            print len(i)
        for i in range(len(self.rows)):
            resPart = []
            for j in range(len(other.cols)):
                resPart.append(self.rows[i].dot(other.cols[j]))
            result.append(Vector(resPart))
        return Matrix(result)

    def __repr__(self):
        return repr(self.rows)
