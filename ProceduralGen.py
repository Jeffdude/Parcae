"""
Central place for procedural generation algorithms

Author: Jeff
"""

import pygame, random
from pygame.locals import *
from color import *

#Global Constants
NULL_HEIGHT = -1

DEBUG_BOOL = False

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

def diamondSquare(wDimensions, heightMap, randMagnitude):
    global NULL_HEIGHT # used to prevent overwritten information
    # define side lengths
    xDim, yDim = wDimensions
    if xDim != yDim:
        raise ValueError("DS Algorithm doesn't know how to handle rectangles yet")
    sideLength = xDim - 1

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
                    heightMap[x][y] = eVal

        randMagnitude /= 2
        sideLength = int(sideLength/2)
    
    return heightMap


    
    
def pcgDiamondSquare(wWidth, wHeight, maxMagnitude):
    # ensure / fix dimensions to be in the form of 2^n + 1
    worldWidth, worldHeight = getProperDimensions(wWidth, wHeight)
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
    return diamondSquare(worldDimensions, heightMap, maxMagnitude)

