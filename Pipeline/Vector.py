# This is a class to make vector math, and working with vectors easy.
# Written by Murphy Randle, 2012: murphyrandle@gmail.com
# Heavily referenced from: http://www.math.okstate.edu/~ullrich/PyPlug/

class Vector(object):
    def __init__(self, *indata):
        # This is to check if the args are a list, or just values.
        if (len(indata) > 0):
            if (type(indata[0]) == type([])) or \
               (type(indata[0]) == type(())):
                indata = indata[0]
        self.data = indata

        # If the vector has three dimensions, break it up.
        if (len(self.data) == 3):
            self.x = self.data[0]
            self.y = self.data[1]
            self.z = self.data[2]

    def __repr__(self):
        return repr(self.data)

    def __add__(self, other):
        result = []
        for i in range(len(self.data)):
            result.append(self.data[i] + other.data[i])
        return Vector(result)

    def __getitem__(self, index):
            return self.data[index]

    def __len__(self):
        return len(self.data)

    def dot(self, other):
        # This will provide the dot product of the vector.
        result = []
        for i in range(len(self.data)):
            result.append(self.data[i] * other.data[i])
        return sum(result)

    def cross(self, other):
        # This should only be used with a 3 dimensional vector.
        # Returns the vector result of the cross product.
        newX = (self.y * other.z) - (self.z * other.y)
        newY = (self.z * other.x) - (self.x * other.z)
        newZ = (self.x * other.y) - (self.y * other.x)
        return Vector(newX, newY, newZ)
