"""
procedural generation of noise for the Parcae landscape
"""
import noise, random
import numpy as np

random.seed()

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
    

    rand_offset = random.random()
    max_height = 0.0
    denom = 315.0
    # generate the noise
    for x in range(len(landscape)):
        for y in range(len(landscape[0])):
            height = noise.snoise2(
                    x / denom + 0.5 + rand_offset, 
                    y / denom + 0.5 + rand_offset, 
                    octaves=3, persistence=0.65, lacunarity=1.5)\
                            * 10 + 10
            landscape[x][y] = height
            if height > max_height:
                max_height = height
    return (landscape, max_height)

class landscape_change:
    def __init__(self, heightMap, totalFrames, noise_type="simplex"):
        """
        calculates the transition states and stores them as numpy arrays

        heightMap -- the original land map before the transition
        totalFrames -- the desired number of states to calculate throughout the
        transition
        """
        if noise_type not in ["simplex", "perlin"]:
            error = "# invalid noise_type"
            print(error)
            raise ValueError(error)
        return

    def getFrame(self, frameNumber):
        return
