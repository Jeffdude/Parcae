"""
Central place for procedural generation algorithms

Author: Jeff M -- jeffmilling/gmail/com
"""

import pygame, random
from pygame.locals import *
from color import *
#------------------------------------------------------------------------------
# Global Constants
#------------------------------------------------------------------------------
NULL_HEIGHT = -1
        
TRACK_MAX = False
MAX_HEIGHT = 0

DEBUG_BOOL = False

#------------------------------------------------------------------------------
# Helper Functions
#------------------------------------------------------------------------------

def getProperDimensions(worldWidth, worldHeight):
    tempWidth = 1
    tempHeight = 1
    while tempWidth < worldWidth - 1:
        tempWidth <<= 1
    while tempHeight < worldHeight - 1:
        tempHeight <<= 1
    return (tempWidth + 1, tempHeight + 1)

def debug():
    global DEBUG_BOOL
    return DEBUG_BOOL


def trackMax():       # the max height is useful for rendering the map
    global TRACK_MAX
    return TRACK_MAX

def pcgGetMaxHeight():   
    """
    Small helper function that returns the max height in the last generator
    function
     - resets MAX_HEIGHT and TRACK_MAX to 0 and False
    """
    global MAX_HEIGHT
    global TRACK_MAX
    if trackMax():
        TRACK_MAX = False
        temp = MAX_HEIGHT
    else:
        return 0
#------------------------------------------------------------------------------
# Diamond Square Algorithm
#------------------------------------------------------------------------------
   

def _diamondSquare(wDimensions, heightMap, randMagnitude, randState=None):
    global NULL_HEIGHT # used to prevent overwritten information
    if trackMax():
        global MAX_HEIGHT # need global var to track max

    # define side lengths
    xDim, yDim = wDimensions
    if xDim != yDim:
        raise ValueError("DS Algorithm doesn't know how to handle rectangles yet")
    sideLength = xDim - 1
    if randState is not None:
        random.setstate(randState)

    # square
    while sideLength >= 2:
        centerLength = int(sideLength / 2)
        if debug():
            print('sideLength: {}'.format(sideLength))
            print('centerLength: {}'.format(centerLength))
        # square
        for x in range(0, xDim - 1, sideLength):
            for y in range(0, yDim - 1, sideLength):
                # get average values for corner
                cornerAverage = heightMap[x][y] 
                cornerAverage += heightMap[x + sideLength][y]
                cornerAverage += heightMap[x][y + sideLength]
                cornerAverage += heightMap[x + sideLength][y + sideLength]
                cornerAverage /= 4
                if debug():
                    print('cAve {}'.format(cornerAverage))

                # assign center value
                cVal = cornerAverage + (random.random() * randMagnitude)
                if heightMap[x + centerLength][y + centerLength] == NULL_HEIGHT:
                    if debug():
                        print('center {}'.format(cVal))
                    if trackMax():
                        if cVal > MAX_HEIGHT:
                            MAX_HEIGHT = cVal
                    heightMap[x + centerLength][y + centerLength] = cVal

        # diamond
        for x in range(0, xDim, centerLength):
            for y in range((x + centerLength) % sideLength, yDim, sideLength):
                # left of center
                edgeAverage = heightMap[(x - centerLength + xDim - 1) % xDim - 1][y]
                # right of center
                edgeAverage += heightMap[(y + centerLength) % xDim - 1][y]
                # below center
                edgeAverage += heightMap[x][(y + centerLength) % yDim - 1]
                # above center
                edgeAverage += heightMap[x][(y - centerLength + yDim - 1) % yDim - 1]
                edgeAverage /= 4
                if debug():
                    print('eAve {}'.format(edgeAverage))

                eVal = edgeAverage + (random.random() * randMagnitude)
                if heightMap[x][y] == NULL_HEIGHT:
                    if debug():
                        print('edge {}'.format(eVal))
                        print('  writing to: {},{}'.format(x,y))
                    if trackMax():
                        if eVal > MAX_HEIGHT:
                            MAX_HEIGHT = eVal
                    heightMap[x][y] = eVal

        randMagnitude /= 2
        sideLength = int(sideLength/2)
    
    return heightMap

    
def pcgDiamondSquare(wWidth, wHeight, maxMagnitude, randState=None,
        getMaxHeight=False):
    """
    public interface for diamondSquare heightmap generator
    """
    # ensure / fix dimensions to be in the form of 2^n + 1
    worldWidth, worldHeight = getProperDimensions(wWidth, wHeight)
    # debug and max height
    if getMaxHeight:
        global TRACK_MAX 
        TRACK_MAX = True
    if debug():
        print('wWidth: {} wHeight: {}'.format(worldWidth, worldHeight))
    # create the map
    global NULL_HEIGHT
    heightMap = [[NULL_HEIGHT for x in range(worldWidth)] for x in range(worldHeight)]

    # firstly, randomly seed the corner values:
    tl = (0, 0)
    tr = (0, worldWidth - 1)
    bl = (worldHeight - 1, 0)
    br = (worldHeight - 1, worldWidth - 1)
    heightMap[tl[0]][tl[1]] = maxMagnitude * random.random()
    heightMap[tr[0]][tr[1]] = maxMagnitude * random.random()
    heightMap[bl[0]][bl[1]] = maxMagnitude * random.random()
    heightMap[br[0]][br[1]] = maxMagnitude * random.random()

    # begin diamond square algorithm
    worldDimensions = (worldWidth, worldHeight)
    return _diamondSquare(worldDimensions, heightMap, maxMagnitude,
            randState)
#------------------------------------------------------------------------------
# Random Sampling Algorithm
#------------------------------------------------------------------------------

def isValidPoint(prev_coords, cur_coord, min_distance, min_distance_sq):
    if min_distance_sq is None:
        min_distance_sq = min_distance * min_distance 
    for i_coord in prev_coords:
        if i_coord[0] == cur_coord[0]:
            return fabs(i_coord[1] - cur_coord[1]) > min_distance
        elif i_coord[1] == cur_coord[1]:
            return fabs(i_coord[0] - cur_coord[0]) > min_distance
        else:
            xdiff = fabs(i_coord[0] - cur_coord[0])
            ydiff = fabs(i_coord[1] - cur_coord[1])
            return (xdiff * xdiff) + (ydiff * ydiff) > min_distance_sq
    return True


def pcgRandomPoints(wDim, numPoints=10, minDistance=50,
        randState=None):
    """
    return list of a random sampling of <numPoints> positions in 
    a 2d world with dimensions wDim (x,y)
    """
    (wWidth, wHeight) = wDim
    if randState is not None:
        random.setstate(randState)
    else:
        random.seed()
    min_distance_sq = min_distance * min_distance
    points = []
    n = 0
    while n < numPoints:
        pt_coord = (random.randint(0, wWidth), random.randint(0, wHieght))
        if isValidPoint(points, pt_coord, minDistance, min_distance_sq):
            points.append(pt_coord)
            n+=1
    return points
