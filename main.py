"""
Main file of my experiment with procudurally generated dangers

Author: Jeff M -- jeffmilling/gmail/com
"""
import pygame, random, sys
from pygame.locals import *
from render import *
from ProceduralGen import *

# Defining global constants
import settings 

#------------------------------------------------------------------------------
# Initialize the world
#------------------------------------------------------------------------------
def initWorld(maxMagnitude=100, worldSeed=None):
    """
    Set up the Parcae landscape 
    """
    # Get proper dimensions
    #   defined by the closest numerical values 
    #   of 2^n to the display resolution
    tempWidth = tempHeight = 1
    (worldWidth,worldHeight) = settings.DISP_DIM
    while tempWidth < worldWidth:
        tempWidth <<= 1
    while tempHeight < worldHeight:
        tempHeight <<= 1
    # Since DS algorithm can not handle rectangles, world can be larger than
    # the display and some will simply be cut off
    worldSize = int(max(tempWidth, tempHeight))
    if settings.DEBUG:
        print(">   Display Dimensions: ({},{})".format(worldWidth, worldHeight))
        print(">   World Edge Size: {}".format(worldSize))
    settings.WORLD_DIM = (worldSize + 1, worldSize + 1)

    # Create initial landscale from seed value if it is defined
    if worldSeed is not None:
        random.seed(worldSeed)
    else: # default to system time
        random.seed()
    settings.WORLD = pcgDiamondSquare(settings.WORLD_DIM[0], settings.WORLD_DIM[1], 
            maxMagnitude, random.getstate())
    settings.W_MAX_HEIGHT = getLastMaxHeight()
    if settings.DEBUG:
        print(">  Terrain max height: {}".format(settings.W_MAX_HEIGHT))

#------------------------------------------------------------------------------
# Parcae Life Loop
#------------------------------------------------------------------------------
def lifeLoop():
    """
    Parcae's life loop is the central control of each occurance in the Parcae
    environment

    Should handle landscape updates, species life/death, and keyboard input
    """
    return None

#------------------------------------------------------------------------------
# Initialize Parcae environment and call life loop
#------------------------------------------------------------------------------
def main():
    """
    Main function
    """
    # Disable fullscreen, set dimensions
    n = 4
    displayEdgeSize = int(2**n + 1)
    if settings.DEBUG:
        print(">   Display Edge Size: {}".format(displayEdgeSize))
    settings.DISP_DIM=(displayEdgeSize, displayEdgeSize)

    initWindow(fullscreen=False)
    initWorld()
    initRenderLandscape()
    
    lifeLoop()
    
    
if __name__ == "__main__":
    main()
