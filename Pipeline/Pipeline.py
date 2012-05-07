from Matrix import Matrix
from Vector import Vector
from Camera import Camera
from Point import Point
import math


def GetScreenCoords(point, cam, imageX, imageY):
    t = abs(cam.n) * math.tan(math.radians(cam.angle / 2))
    b = -t
    r = t * imageX / imageY
    l = -r

    Morth1 = Matrix(
        [imageX / 2.0    ,0.0  ,0.0  ,(imageX - 1.0) / 2.0  ],
        [0.0  ,imageY / 2.0    ,0.0    ,(imageY - 1.0) / 2.0  ],
        [0.0    ,0.0    ,1.0    ,0.0    ],
        [0.0    ,0.0    ,0.0    ,1.0    ]
        )

    Morth2 = Matrix(
                [2.0 / (r - l),            0,            0,            0],
                [0            ,2.0 / (t - b),            0,            0],
                [0            ,0            ,2.0 / (cam.n - cam.f),    0],
                [0            ,            0,            0,            1]
                )

    Morth3 = Matrix(
                [1,         0,          0,      (- (l + r) / 2)],
                [0,         1,          0,      (- (b + t) / 2)],
                [0,         0,          1,      (- (cam.n + cam.f) / 2)],
                [0,         0,          0,      1]
                )

    Morth = Morth1 * Morth2 * Morth3

    MvScale = Matrix(
                [cam.u.x, cam.u.y, cam.u.z, 0],
                [cam.v.x, cam.v.y, cam.v.z, 0],
                [cam.w.x, cam.w.y, cam.w.z, 0],
                [0, 0, 0, 1]
                )
    MvTrans = Matrix(
                [1, 0, 0, -1.0 * cam.e.x],
                [0, 1, 0, -1.0 * cam.e.y],
                [0, 0, 1, -1.0 * cam.e.z],
                [0, 0, 0, 1],
                )
    Mv = MvScale * MvTrans

    Mp = Matrix(
            [1, 0, 0, 0],
            [0, 1, 0, 0],
            [0, 0, (cam.n + cam.f) / cam.n, -1 * cam.f],
            [0, 0, (1 / cam.n), 0]
            )

    M = Morth * Mp * Mv

    result = M * point
    result = result / result.h
    return result

if __name__ == "__main__":
    # Image dimensions:
    imageX = 800
    imageY = 600

    print """
    # Image dimensions:
    imageX = 800
    imageY = 600

    # The correct answers are pulled from the slides, estimated conceptually, 
    # and inspired by modeling the situation in a 3d package.
    """

    print """
    # Camera sitting, looking down negative Y. Coords are (0, 1, 0) 
    # Up vector is (1, 1, 0)
    # Object should sit at about center screen, or (400, 600).
    point = Point(0, -3, 0)
    """
    point = Point(0, -3, 0)
    cam = Camera()
    cam.eSet(0.0, 1.0, 0.0)
    cam.gSet(0.0, -1.0, 0.0)
    cam.tSet(1.0, 1.0, 0.0)
    cam.angleSet(30.0)
    cam.nSet(-2.0)
    cam.fSet(-200.0)
    print GetScreenCoords(point, cam, imageX, imageY)

    print """
    # Same camera to point relationship, but this time the camera is looking
    # down negative the Z. 
    # Eye position: (0, 0, 1)
    # Gaze: (0, 0, -1)
    # Up: (0, 1, 0)
    # Angle: 30 Degrees.
    # Near -2, and far -200.
    # Point is at: (0, 0, -3). Values should be the same as the example above.
    """
    point = Point(0, 0, -3)
    cam = Camera()
    cam.eSet(0, 0, 1)
    cam.gSet(0, 0, -1)
    cam.tSet(0, 1, 0)
    cam.angleSet(30.0)
    cam.nSet(-2.0)
    cam.fSet(-200.0)
    print GetScreenCoords(point, cam, imageX, imageY)

    print """
    # Point moved to the left, and onto the clipping plane.
    # Using the same camera as the last example, the Point's coordinates
    # should be close to 0 in x, and about 300 in y.
    # Point's corrdinates are: (-0.714, 0, -1)
    """
    point = Point(-0.714, 0, -1)
    print GetScreenCoords(point, cam, imageX, imageY)

    print """
    # Same camera as before, and the point is on the clipping plane, but 
    # adjusted up and to the left so that the coordinates in x should be 
    # about 0 and the coordinates in y should be about 600.
    # Point's coordinates are: (-0.714, 0.535, -1)
    """
    point = Point(-0.714, 0.535, -1)
    print GetScreenCoords(point, cam, imageX, imageY)

