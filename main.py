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
    settings.WORLD_DIM = (tempWidth + 1, tempHeight + 1)

    # Create initial landscale from seed value if it is defined
    if worldSeed is not None:
        random.seed(worldSeed)
    else: # default to system time
        random.seed()
    settings.WORLD = pcgDiamondSquare(settings.WORLD_DIM[0], settings.WORLD_DIM[1], 
            maxMagnitude, random.getstate())
    settings.W_MAX_HEIGHT = pcgGetMaxHeight()

#------------------------------------------------------------------------------
# Initialize Parcae environment and call life loop
#------------------------------------------------------------------------------
def main():
    """
    Main function
    """
    # Disable fullscreen, set dimensions
    n = 5
    settings.DISP_DIMENSIONS=(2**n + 1, 2**n + 1)

    initWindow()
    initWorld()
    initRenderLandscape()
    
    
if __name__ == "__main__":
    main()
