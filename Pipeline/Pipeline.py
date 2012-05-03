from Matrix import Matrix

# Set up point values:
gPoint = [1, 2, 3]
gCam = {}
gCam['position'] = [3, 2, 0]
gCam['rotation'] = [3, 2, 10]
gImage = {}
gImage['x'] = 800
gImage['y'] = 600

Mvp = Matrix(
    [gImage['x']/2, 0            , (gImage['x']-1)/2],
    [0            , gImage['y']/2, (gImage['y']-1)/2],
    [0            , 0            , 1                ]
    )