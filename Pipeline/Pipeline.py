from Matrix import Matrix
from Vector import Vector

# Set up point values:
gPoint = Vector(1, 2, 3, 1)
gPoint2 = Matrix(
            [1],
            [2],
            [3],
            [1]
            )
gCam = {}
gCam['position'] = Vector(3, 2, 0)
gCam['rotation'] = Vector(3, 2, 10)
gImage = {}
gImage['x'] = 800
gImage['y'] = 600
l = b = f = -20
r = t = n = 20



Mvp = Matrix(
    [gImage['x']/2, 0            , 0    , (gImage['x']-1)/2],
    [0            , gImage['y']/2, 0    , (gImage['y']-1)/2],
    [0            , 0            , 1    , 0                ],
    [0            , 0            , 0    , 1                ]
    )

Morth = Matrix(
        [2 / (r - l), 0, 0, (-(r+l)/(r-l))],
        [0, 2 / (t-b), 0,   (-(t+b)/(t-b))],
        [0, 0, 0, 2/(n-f),  (-(n+f)/(n-f))],
        [0, 0,  0,  1]
        )

if __name__ == "__main__":
    # print "Point position in world space: "
    # print Mvp * gPoint
    a = Matrix(
            [1, 2, 3],
            [4, 5, 5],
            [6, 2, 1]
            )
    b = Matrix(
            [-1, 2, 4],
            [5, 6, 2],
            [9, 5, 1]
            )
    print a * b
