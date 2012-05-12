import bge
from MTools.Vector import Vector as MVector
from math import *


class Joint(object):
    def __init__(self, obj, child=None, length=10):
        self.o = obj
        self.child = child
        self.length = length

    def setWorldOrientation(self, val):
        self.o.worldOrientation = (0, 0, val)
        self.updateChildren()

    def setWorldPosition(self, *vals):
        self.o.worldPosition = vals
        self.updateChildren()

    def rotateRelative(self, rot):
        self.o.applyRotation([0, 0, rot])
        self.updateChildren(rot)

    def updateChildPos(self):
        # Moves the child object
        newPos = self.endPos()
        self.child.setWorldPosition(*newPos)

    def updateChildRot(self, rot):
        # Rotates the child object
        self.child.rotateRelative(rot)


    def endPos(self):
        # Calculates the world space position at the end of this vector
        # based upon the world position of the parent.
        rotation = self.o.worldOrientation.to_euler().z
        x = self.o.position.x + self.length * cos(rotation)
        y = self.o.position.y + self.length * sin(rotation)
        return MVector([x, y, 0])

    def updateChildren(self, rot=0):
        if(self.child):
            self.updateChildRot(rot)
            self.updateChildPos()
