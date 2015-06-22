import pygame
from pygame.locals import *
from ProceduralGen import *
import settings # access globals
from color import * # color helper functions
if settings.DEBUG > 2:
    import time
#------------------------------------------------------------------------------
# Setting up the window
#------------------------------------------------------------------------------

def initWindow(fullscreen=True):
    """ 
    Set up pygame window
    defaults to fullscreen mode
    """
    if settings.DEBUG: print("~ Initializing pygame window") 
    pygame.init()
    pygame.display.set_caption('Parcae')
    dispInfo = pygame.display.info()
    dispStyle = None
    if(fullscreen):
        if settings.DEBUG: print("~ Pygame window is fullscreen") 
        dispStyle = pygame.FULLSCREEN | pygame.HWSURFACE | pygame.DOUBLEBUF
        settings.DISP_DIM = (dispInfo.current_h, disp_info.current_w)
        if settings.DEBUG > 1:
            print(">   Display Height: {}".format(dispInfo.current_h))
            print(">   Display Width: {}".format(dispInfo.current_w))
    SCREEN = pygame.display.set_mode(settings.DISP_DIM, dispStyle)
    SCREEN.set_alpha(None)
    SCREEN.fill(BLACK)
    if settings.DEBUG: print("~ Done initializing pygame window") 

#------------------------------------------------------------------------------
# Rendering and helper functions
#------------------------------------------------------------------------------
def makeColor(toColorize):
    if toColorize <= settings.W_MAX_HEIGHT:
        return colorGenRGB(toColorize, 0, settings.W_MAX_HEIGHT)
    else:
        print("# Color exceeds max colorizable value")
        return (0,0,0)

def initRenderLandscape():
    if settings.DEBUG: print("~ Beginning initial render") 
    if settings.DEBUG > 2: 
        renderStart = time.clock()

    for x in range(settings.WORLD.len):
        for y in range(settings.WORLD[0].len):
            coord_color = makeColor(settings.WORLD[x][y])
            settings.SCREEN.set_at((x,y), coord_color)

    if settings.DEBUG > 2:
        renderStop = time.clock()
        print(">>   Initial Render took {} seconds".format(
            round(renderStop - renderStart, 4) ))

#def updateWindow(dirty_rects):
#    """ dirty_rects is a rectangle or list of rectangles that will be refreshed
#    on screen
#    """
