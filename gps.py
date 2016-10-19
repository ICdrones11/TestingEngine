#!/usr/bin/python
import math
from vector import *

EARTH_RADIUS = 6398000  #Earth radius in meters

# Calculations in this module implemented using equations at:
# http://www.geom.uiuc.edu/docs/reference/CRC-formulas/node42.html

# Calculate the terrestrial location
def computeTerrestrialCoordinates(polarCoordinates):
    lon, lat, alt = polarCoordinates.unbox()
    lonRad = math.radians(lon)
    latRad = math.radians(lat)

    h = EARTH_RADIUS + alt
    tx = h * math.sin(latRad) * math.cos(lonRad)
    ty = h * math.sin(latRad) * math.sin(lonRad)
    tz = h * math.cos(latRad)
    #print 'Computed terrestrial coordinates: {}, {}, {}\n'.format(tx,ty,tz)
    return Vector(tx, ty, tz)

# Calculate polar coordinates from terrestrial ones.
def computePolarCoordinates(terrestrialCoordinates):
    tx, ty, tz = terrestrialCoordinates.unbox()
    r = math.sqrt(tx**2 + ty**2 + tz**2)
    lat = math.degrees(math.asin(tz / r))
    lon = math.degrees(math.atan(ty / tx))
    alt = r - EARTH_RADIUS
    return Vector(lon, lat, alt)

# Switch to terrestrial location, move, and switch back.
def computeNextPolarLocation(velocityVector, polarCoordinates):
    terrestrialLocation = computeTerrestrialCoordinates(polarCoordinates)
    newTerrestrialLocation = terrestrialLocation + velocityVector
    # nx, ny, nz = newTerrestrialLocation.unbox()
    # print 'Computed next location: {}, {}, {}\n'.format(nx, ny, nz)
    return computePolarCoordinates(newTerrestrialLocation)
