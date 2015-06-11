import pygame
from pygame.locals import *
from ProceduralGen import *
import settings #access globals
#------------------------------------------------------------------------------
# Setting up the window
#------------------------------------------------------------------------------

def initWindow(fullscreen=True):
    """ 
    Set up pygame window
    in fullscreen mode
    """
    print("~ Initializing pygame window")
    pygame.init()
    pygame.display.set_caption('Parcae')
    dispInfo = pygame.display.info()
    dispStyle = None
    if(fullscreen):
        print("~ Pygame window is fullscreen")
        dispStyle = pygame.FULLSCREEN|pygame.HWSURFACE|pygame.DOUBLEBUF
        settings.DISP_DIM = (dispInfo.current_h, disp_info.current_w)
    SCREEN = pygame.display.set_mode(settings.DISP_DIM, dispStyle)
    SCREEN.fill(BLACK)
    print("~ Done")

def renderLandscape():
    for x in range(settings.WORLD.len):
        for y in range(settings.WORLD[].len):
            #TODO
