import bge
from mathutils import *
from math import *


class Joint(object):
    def __init__(self, obj, parent=None, child=None, length=10):
        self.o = obj
        self.parent = parent
        self.child = child
        self.orient = 0.0
        self.length = length

    def setWorldOrientation(self, *vals):
        self.o.worldOrientation = vals
        if(self.child):
            self.updateChildPos(self.child)

    def setWorldPosition(self, *vals):
        self.o.worldPosition = vals
        if(self.child):
            self.updateChildPos(self.child)

    def updateChildPos(self, joint):
        # Moves the child object
        joint.setWorldPosition(*(self.o.worldPosition + self.endPos(self)))

    def endPos(self, joint):
        # Calculates the world space position at the end of this vector
        # based upon the world position of the parent.
        x = joint.length * cos(joint.orient)
        y = joint.length * sin(joint.orient)
        return Vector([x, y, 0])
