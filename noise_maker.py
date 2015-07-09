"""
procedural generation of noise for the Parcae landscape
"""
import noise, random
import numpy as np

def perlinNoise(wWidth, wHeight):
    """
    wrapper for 'noise' packages pnoise2 function
    """
    # create the map
    landscape = np.empty((wWidth, wHeight), dtype=np.float)
    landscape.fill(-1)
    

    max_height = 0.0
    denom = 16.0
    # generate the noise
    for x in range(len(landscape)):
        for y in range(len(landscape[0])):
            height = noise.pnoise2(x / denom, y / denom) * 10 + 10
            landscape[x][y] = height
            if height > max_height:
                max_height = height
    return (landscape, max_height)

def simplexNoise(wWidth, wHeight):
    """
    wrapper for 'noise' packages pnoise2 function
    """
    # create the map
    landscape = np.empty((wWidth, wHeight), dtype=np.float)
    landscape.fill(-1)
    

    max_height = 0.0
    denom = 16.0
    # generate the noise
    for x in range(len(landscape)):
        for y in range(len(landscape[0])):
            height = noise.snoise2(x / denom, y / denom) * 10 + 10
            landscape[x][y] = height
            if height > max_height:
                max_height = height
    return (landscape, max_height)
