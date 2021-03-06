#!/usr/bin/env python
"""
These functions, when given a magnitude mag between cmin and cmax, return
a colour tuple (red, green, blue). Light blue is cold (low magnitude)
and yellow is hot (high magnitude).

"""
import math

def floatRgb(mag, cmin, cmax):
       """
       Return a tuple of floats between 0 and 1 for the red, green and
       blue amplitudes.
       """

       try:
              # normalize to [0,1]
              x = float(mag-cmin)/float(cmax-cmin)
       except:
              # cmax = cmin
              x = 0.5
       blue = min((max((4*(0.75-x), 0.)), 1.))
       red  = min((max((4*(x-0.25), 0.)), 1.))
       green= min((max((4*math.fabs(x-0.5)-1., 0.)), 1.))
       return (red, green, blue)

def colorGenRGB(mag, cmin, cmax):
       """
       Return a tuple of integers to be used in AWT/Java plots.
       """

       red, green, blue = floatRgb(mag, cmin, cmax)
       return (int(red*255), int(green*255), int(blue*255))

def grayscale(mag, cmin, cmax):
    """
    Returns a 3-tuple of integers to be used in terrain generation
    """
    if mag > cmax or mag < cmin:
        return (0, 0, 0)
    scale = float(cmax - cmin)
    frac = (mag - cmin) / scale
    return (frac * 255, frac * 255, frac * 255)


