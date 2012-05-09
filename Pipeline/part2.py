# This script is meant to be run with processing.py
# It will not work with the standard python interpreter.
from Pipeline import *
from Vector import *
from Camera import *
from Point import *

persp = Persp()

def setup():
    imageX = 800
    imageY = 600
    size(imageX, imageY)
    stroke(192)

def drawCube(x, y, z, scale):
    A = Point(x + (-scale), y + scale, z + (-scale))
    B = Point(x + scale, y + scale, z + (-scale))
    C = Point(x + scale, y + scale, z + scale)
    D = Point(x + (-scale), y + scale, z + scale)
    E = Point(x + (-scale), y + (-scale), z + (-scale))
    F = Point(x + scale, y + (-scale), z + (-scale))
    G = Point(x + scale, y + (-scale), z + scale)
    H = Point(x + (-scale), y + (-scale), z + scale)

    top = [A, B, C, D]
    bottom = [E, F, G, H]
    allParts = [top, bottom, [A, E], [B, F], [C, G], [D, H]]
    for part in allParts:
        drawLines(part)

def drawLines(points):
    for i in range(len(points)):
        j = (i + 1) % len(points)
        p1 = persp.findPoint(points[i])
        p2 = persp.findPoint(points[j])
        line(p1.x, p1.y, p2.x, p2.y)

def keyPressed():
    factor = 0.5
    rotFactor = 0.25 * factor

    if (key == ord('j')):
        persp.cam.nudgePos(-factor, 0, 0)

    if (key == ord('l')):
        persp.cam.nudgePos(factor, 0, 0)

    if (key == ord('i')):
        persp.cam.nudgePos(0, -factor, 0)

    if (key == ord('k')):
        persp.cam.nudgePos(0, factor, 0)

    if (key == ord('u')):
        persp.cam.nudgePos(0, 0, -factor)

    if (key == ord('h')):
        persp.cam.nudgePos(0, 0, factor)

    if (key == ord('s')):
        persp.cam.nudgeGaz(-rotFactor, 0, 0)

    if (key == ord('f')):
        persp.cam.nudgeGaz(rotFactor, 0, 0)

    if (key == ord('e')):
        persp.cam.nudgeGaz(0, -rotFactor, 0)

    if (key == ord('d')):
        persp.cam.nudgeGaz(0, rotFactor, 0)

    if (key == ord('r')):
        persp.cam.nudgeT(-rotFactor, 0, 0)

    if (key == ord('w')):
        persp.cam.nudgeT(rotFactor, 0, 0)


def draw():
    background(42, 42, 42)
    drawCube(0, 0, -6, 1)
    drawCube(3, 0, -6, 1)
    drawCube(-3, 0, -6, 1)
    drawCube(0, 3, -6, 1)
    drawCube(0, -3, -6, 1)
