"""
Procedural modifications of the 2D landscape in Parcae

These functions do not necessarily generate landscapes, but they modify them
"""
from ProceduralGen import *

def asteroidMod(world, worldDim, radius=50, additive=False):
    """
    Asteroid modification takes a random sample of locations, and either
    impacts an asteroid, negatively affecting landscape height in its radius
    or lands an asteroid, positively affecting height

    function is basic x^2 + y^2, where x and y are distance from the center of
    the impact, decided by randPoints
    """

    modSize = 2*radius # commonly used value to limit iterations
    # In order to make the impact circular, we must zero out the corners of the
    # x^2 + y^2 function
    maxDepth = radius**2 

    # generate asteroid divet/bump
    modArray[[for i in range(modSize)] for j in range(modSize)]
    for x in range(modSize):
        for y in range(modSize):
            diff = (x-radius)**2 + (y-radius)**2
            if diff > maxDepth:
                diff = 0            # corner location 
            if additive:
                modArray[x][y] += diff
            else:
                modArray[x][y] -= diff

    # apply asteroid affect to randPoints in world
    numPoints = 10
    randPoints = pcgRandomPoints(worldDim, numPoints, radius)
    for pnt in randPoints:
        for x in range(modSize):
            for y in range(modSize):
                wx = pnt[0] - x
                wy = pnt[1] - y
                if wx > 0 and wy > 0 and wx < worldDim[0] and wy < worldDim[1]:
                    world[wx][wy] += modArray[x][y]

