import bge
from math import *
from Joint import *
from MTools.Matrix import Matrix as MMatrix
from MTools.Vector import Vector as MVector

# Set up some globals.
cont = bge.logic.getCurrentController()
root = cont.owner
rasterizer = bge.render

def main():
    # Get some basic objects set up.
    scene = bge.logic.getCurrentScene()
    objects = scene.objects
    suzy = scene.objects['suzy']
    rasterizer.showMouse(True)

    # Build a list of all of my joints.
    joints = [Joint(objects['j'+str(i)]) for i in range(0,4)]
    # Connect up child relationships
    for i in range(0,3):
        joints[i].child = joints[i + 1]

    #Compute the jacobian, and build a new vector with the rotation values in it. (Rotations are relative to parent)
    jacobian = buildJacobian(joints)
    changeVector = findChangeVector(joints, suzy)
    rotations = jacobian * changeVector
    # Scale the rotations down to an acceptable value.
    rotations *= 0.0007

    jointsAndRots = list(zip(joints, rotations))
    [x[0].rotateRelative(x[1]) for x in jointsAndRots]

def buildJacobian(joints):
    # Cross (0, 0, 1) with 3 difference vectors
    # Jacobian is made of those vectors. 
    # transpose it before returning.
    upVector = MVector(0, 0, 1)
    endEffector = joints[len(joints) - 1]
    products = []
    for i in range(len(joints) - 1):
        difVec = endEffector.o.position - joints[i].o.position
        products.append(upVector.cross(difVec))
    result = MMatrix(products[0], products[1], products[2])
    result = result.transpose()
    return result

def findChangeVector(joints, target):
    # Find the vector between the end effector and the target.
    endEffector = joints[len(joints) - 1]
    vector = MVector(*(target.position - endEffector.o.position))
    return vector

main()
