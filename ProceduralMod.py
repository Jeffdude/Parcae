"""
Procedural modifications of the 2D landscape in Parcae
"""
from ProceduralGen import *

def asteroidMod(world, worldDim, maxMagnitude=100, radius=50):
    """
    Asteroid modification takes a random sample of locations, and either
    impacts an asteroid, negatively affecting landscape height in its radius
    or lands an asteroid, positively affecting height
    """
    randPoints = pcgRandomPoints(worldDim, 10, radius)
    for pnt in randPoints:


