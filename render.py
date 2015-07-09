import pygame
from pygame.locals import *
from ProceduralGen import *
import settings # access globals
from color import * # color helper functions
if settings.DEBUG > 2:
    import time
NUM_ERRORS = 0
#------------------------------------------------------------------------------
# Setting up the window
#------------------------------------------------------------------------------

def initWindow(fullscreen=False):
    """ 
    Set up pygame window
    default to windowed mode
    """
    if settings.DEBUG: print("~ Initializing pygame window") 
    pygame.init()
    pygame.display.set_caption('Parcae')
    dispInfo = pygame.display.Info()
    if settings.DEBUG > 1:
        print(">   Display Height: {}".format(dispInfo.current_h))
        print(">   Display Width: {}".format(dispInfo.current_w))
    dispStyle = 0
    if(fullscreen):
        if settings.DEBUG: print("~ Pygame window is fullscreen") 
        dispStyle = pygame.FULLSCREEN | pygame.HWSURFACE | pygame.DOUBLEBUF
        settings.DISP_DIM = (dispInfo.current_h, dispInfo.current_w)
    settings.SCREEN = pygame.display.set_mode(settings.DISP_DIM, dispStyle)
    settings.SCREEN.set_alpha(None)
    settings.SCREEN.fill(settings.BLACK)
    if settings.DEBUG: print("~ Done initializing pygame window") 

#------------------------------------------------------------------------------
# Rendering and helper functions
#------------------------------------------------------------------------------
def makeColor(toColorize):
    global NUM_ERRORS
    if toColorize <= settings.W_MAX_HEIGHT:
        return colorGenRGB(toColorize, 0, settings.W_MAX_HEIGHT)
    else:
        if NUM_ERRORS == 0:
            print("# Color exceeds max colorizable value")
            NUM_ERRORS += 1
        return (0,0,0)

def initRenderLandscape():
    if settings.DEBUG: print("~ Beginning initial render") 
    if settings.DEBUG > 2: 
        renderStart = time.clock()

    for x in range(len(settings.WORLD)):
        for y in range(len(settings.WORLD[0])):
            coord_color = makeColor(settings.WORLD[x][y])
            settings.SCREEN.set_at((x,y), coord_color)
    pygame.display.flip()
    if settings.DEBUG > 2:
        renderStop = time.clock()
        print(">>   Initial Render took {} seconds".format(\
                round(renderStop - renderStart, 4)))

#def updateWindow(dirty_rects):
#    """ dirty_rects is a rectangle or list of rectangles that will be refreshed
#    on screen
#    """
