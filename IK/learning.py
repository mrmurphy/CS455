import bge
from mathutils import *
from math import *
from Joint import *
from MTools.Matrix import Matrix
from MTools.Vector import Vector

# Set up some globals.
cont = bge.logic.getCurrentController()
root = cont.owner

def main():
    # Get some basic objects set up.
    scene = bge.logic.getCurrentScene()
    objects = scene.objects
    suzy = scene.objects['suzy']

    # Build a list of all of my joints.
    joints = [Joint(objects['j'+str(i)]) for i in range(0,4)]
    # Connect up child relationships
    for i in range(0,3):
        joints[i].child = joints[i + 1]

    jacobian = buildJacobian(joints)
    print(jacobian)

    # Make some moves happen.
    # sinWav(suzy)
    # track(joints[0], suzy)

def buildJacobian(joints):
    # Cross (0, 0, 1) with 3 difference vectors
    # Jacobian is made of those vectors. 
    # transpose it before returning.
    upVector = Vector(0, 0, 1)
    endEffector = joints[len(joints) - 1]
    products = []
    for i in range(len(joints) - 1):
        difVec = endEffector.o.position - joints[i].o.position
        products.append(upVector.cross(difVec))
    result = Matrix(products[0], products[1], products[2])
    result = result.transpose()
    return result

main()

# def sinWav(what):
#     # Moves an object in simple harmonic motion
#     amp = 10 
#     per = 5
#     # Requires a timer attribute on root object.
#     newY = amp * cos( 2 * pi / 5 * root['timer']) + (pi / 2)
#     what.worldPosition = (what.position[0], newY, 0)

# def track(obj, target):
#     dif = target.position - obj.o.position
#     angle = atan(dif.y / dif.x)
#     obj.orient += angle
#     obj.setWorldOrientation(0, 0, angle)
