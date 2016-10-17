#!/usr/bin/python

import math
from vector import *

EARTH_RADIUS = 6398000 #Earth radius in meters

class Gps: 
    # Calculate the terrestrial location
    def computeTerrestrialCoordinates(self, polarCoordinates):
        px,py,pz = polarCoordinates.unbox()
        h = EARTH_RADIUS + pz
        tx = h * math.cos(py) * math.cos(px)
        ty = h * math.sin(py) * math.sin(px)
        tz = h * math.cos(py)
        #print 'Computed terrestrial coordinates: {}, {}, {}\n'.format(tx,ty,tz)
        return Vector(tx, ty, tz)
    
    # Switch to terrestrial location, move, and switch back.
    def computeNextPolarLocation(self, velocityVector, polarCoordinates):
        terrestrialLocation = self.computeTerrestrialCoordinates(polarCoordinates)
        newTerrestrialLocation = terrestrialLocation + velocityVector
        #nx, ny, nz = newTerrestrialLocation.unbox()
        #print 'Computed next location: {}, {}, {}\n'.format(nx, ny, nz)
        return self.computePolarCoordinates(newTerrestrialLocation)

    # Calculate polar coordinates from terrestrial ones.
    def computePolarCoordinates(self, terrestrialCoordinates):
        tx,ty,tz = terrestrialCoordinates.unbox()
        px = math.sqrt(tx**2 + ty**2 + tz**2)
        py = math.acos(tz/px)
        pz = math.atan(ty/tx)
        return Vector(px, py, pz)

