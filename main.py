"""
Main file of my experiment with procudurally generated dangers

Author: Jeff Milling - jeffmilling/gmail/com
"""
import pygame, random
from pygame.locals import *
from ProceduralGen import *
#------------------------------------------------------------------------------
# Defining Global Constants
#------------------------------------------------------------------------------
SCREEN = None
DISP_DIM = (0,0)

WORLD_DIM = (0,0)
WORLD = None

# Colors
WHITE = (255, 255, 255)
GREEN = (0, 80, 0)
RED = (150, 0, 0)
BLACK = (0, 0, 0)

#------------------------------------------------------------------------------
# Setting up the window
#------------------------------------------------------------------------------
def initWindow(fullscreen=True):
    """ 
    Set up pygame window
    in fullscreen mode
    """
    global SCREEN
    global DISP_DIMENSIONS
    pygame.init()
    pygame.display.set_caption('Parcae')
    dispInfo = pygame.display.info()
    if(fullscreen):
        dispStyle = pygame.FULLSCREEN
        DISP_DIM = (dispInfo.current_h, disp_info.current_w)
    SCREEN = pygame.display.set_mode(DISP_DIM, dispStyle)
    SCREEN.fill(BLACK)

#------------------------------------------------------------------------------
# Initialize the world
#------------------------------------------------------------------------------
def initWorld(maxMagnitude=100):
    """
    Set up the Parcae landscape 
    """
    global WORLD_DIM
    global DISP_DIM
    global WORLD

    # Get proper dimensions
    #   defined by the closest numerical values 
    #   of 2^n to the display resolution
    tempWidth = tempHeight = 1
    (worldWidth,worldHeight) = DISP_DIM
    while tempWidth < worldWidth:
        tempWidth <<= 1
    while tempHeight < worldHeight:
        tempHeight <<= 1
    WORLD_DIM = (tempWidth + 1, tempHeight + 1)

    # Create initial landscale
    WORLD = pcgDiamondSquare(WORLD_DIM[0], WORLD_DIM[1], maxMagnitude)

#------------------------------------------------------------------------------
# Initialize Parcae environment and call life loop
#------------------------------------------------------------------------------
def main():
    """
    Main function
    """
    global DISP_DIMENSIONS
    # Disable fullscreen, set dimensions
    n = 5
    DISP_DIMENSIONS=(2**n + 1, 2**n + 1)

    initWindow(False)
    initWorld()
    
    
    
if __name__ == "__main__":
    main()
