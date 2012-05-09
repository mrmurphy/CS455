from Matrix import Matrix
from Vector import Vector
from Camera import Camera
from Point import Point
import math

class Persp:
    def __init__(self):
        # Set up a camera.
        self.sizeX = 800
        self.sizeY = 600
        self.cam = Camera()
        self.cam.eSet(0, 0, 0)
        self.cam.gSet(0, 0, -1)
        self.cam.tSet(0, 1, 0)
        self.cam.angleSet(50)
        self.cam.nSet(-2)
        self.cam.fSet(-200)

    def findPoint(self, point):
        result = self.GetScreenCoords(point, self.cam, self.sizeX, self.sizeY)
        return result

    def GetScreenCoords(self, point, cam, sizeX, sizeY):
        t = abs(cam.n) * math.tan(math.radians(cam.angle / 2))
        b = -t
        r = t * sizeX / sizeY
        l = -r

        Morth1 = Matrix(
            [sizeX / 2.0    ,0.0  ,0.0  ,(sizeX - 1.0) / 2.0  ],
            [0.0  ,sizeY / 2.0    ,0.0    ,(sizeY - 1.0) / 2.0  ],
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
