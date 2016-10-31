#!/usr/bin/python
import utm

import Constants
from PolarCoordinate import PolarCoordinate


def nextPolar(polarCoordinate, velocity):
    p = utm.from_latlon(polarCoordinate.lat, polarCoordinate.lon)
    nextAltitude = polarCoordinate.alt + velocity.z
    utmEasting = p[0] + Constants.TOWER_LONDON_EASTING + velocity.x
    utmNorthing = p[1] + Constants.TOWER_LONDON_NORTHING + velocity.y
    x, y = utm.to_latlon(utmEasting, utmNorthing, p[2], p[3])
    return PolarCoordinate(x, y, nextAltitude)