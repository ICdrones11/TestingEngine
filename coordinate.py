#!/usr/bin/python import math from vector import build.sh cartesianCoordinate.py config.py coordinate.py droneData droneLogger.py drone.py droneServerMessenger.py droneStatus.py engine.py gps.py polarCoordinate.py README.md testCaseParser.py vector.py velocityCalculator.py visualiser #Mean Earth Radius in m EARTH_RADIUS = 6371000 # Calculations in this module implemented using equations at: # http://www.geom.uiuc.edu/docs/reference/CRC-formulas/node42.html SK = Vector(-0.174685, 51.494150, 200) # Calculate the terrestrial location def computeTerrestrialCoordinates(polarCoordinates): lon, lat, alt = polarCoordinates.unbox() lonRad = math.radians(lon) latRad = math.radians(lat) h = EARTH_RADIUS + alt tx = h build.sh cartesianCoordinate.py config.py coordinate.py droneData droneLogger.py drone.py droneServerMessenger.py droneStatus.py engine.py gps.py polarCoordinate.py README.md testCaseParser.py vector.py velocityCalculator.py visualiser math.sin(latRad) build.sh cartesianCoordinate.py config.py coordinate.py droneData droneLogger.py drone.py droneServerMessenger.py droneStatus.py engine.py gps.py polarCoordinate.py README.md testCaseParser.py vector.py velocityCalculator.py visualiser math.cos(lonRad) ty = h build.sh cartesianCoordinate.py config.py coordinate.py droneData droneLogger.py drone.py droneServerMessenger.py droneStatus.py engine.py gps.py polarCoordinate.py README.md testCaseParser.py vector.py velocityCalculator.py visualiser math.sin(latRad) build.sh cartesianCoordinate.py config.py coordinate.py droneData droneLogger.py drone.py droneServerMessenger.py droneStatus.py engine.py gps.py polarCoordinate.py README.md testCaseParser.py vector.py velocityCalculator.py visualiser math.sin(lonRad) tz = h build.sh cartesianCoordinate.py config.py coordinate.py droneData droneLogger.py drone.py droneServerMessenger.py droneStatus.py engine.py gps.py polarCoordinate.py README.md testCaseParser.py vector.py velocityCalculator.py visualiser math.cos(latRad) #print 'Computed terrestrial coordinates: {}, {}, {}\n'.format(tx,ty,tz) return Vector(tx, ty, tz) # Calculate polar coordinates from terrestrial ones. def computePolarCoordinates(terrestrialCoordinates): tx, ty, tz = terrestrialCoordinates.unbox() r = math.sqrt(tx**2 + ty**2 + tz**2) lat = math.degrees(math.asin(tz / r)) lon = math.degrees(math.atan2(ty, tx)) alt = r - EARTH_RADIUS return Vector(lon, lat, alt) # Switch to terrestrial location, move, and switch back. def computeNextPolarLocation(velocityVector, polarCoordinates): terrestrialLocation = computeTerrestrialCoordinates(polarCoordinates) newTerrestrialLocation = terrestrialLocation + velocityVector # nx, ny, nz = newTerrestrialLocation.unbox() # print 'Computed next location: {}, {}, {}\n'.format(nx, ny, nz) return computePolarCoordinates(newTerrestrialLocation)
#!/usr/bin/python
import math
from vector import *

#Mean Earth Radius in m
EARTH_RADIUS = 6371000

# Calculations in this module implemented using equations at:
# http://www.geom.uiuc.edu/docs/reference/CRC-formulas/node42.html
SK = Vector(-0.174685, 51.494150, 200)


class PolarCoordinate:

    def __init__(self, lat, lon, alt):
        self.position = Vector(lat, lon, alt)

    def lat(self):
        return self.position.x

    def lon(self):
        return self.position.y

    def alt(self):
        return self.position.z

    def unbox(self):
        return self.position.unbox()

    def toCartesian(self):
        lat, lon, alt = self.unbox()
        lonRad = math.radians(lon)
        latRad = math.radians(lat)
        h = EARTH_RADIUS + alt
        x = h * math.sin(latRad) * math.cos(lonRad)
        y = h * math.sin(latRad) * math.sin(lonRad)
        z = h * math.cos(latRad)
        return CartesianCoordinate(x, y, z)


class CartesianCoordinate:

    def __init__(self, x, y, z):
        self.position = Vector(x, y, z)

    def x(self):
        return self.position.x

    def y(self):
        return self.position.y

    def z(self):
        return self.position.z

    def unbox(self):
        return self.position.unbox()

    def nextLocation(self, velocityVector):
        vx, vy, vz = velocityVector.unbox()
        x, y, z = self.unbox()
        newX = x + vx
        newY = y + vy
        newZ = z + vz
        return CartesianCoordinate(newX, newY, newZ)

    def toPolar(self):
        x, y, z = self.unbox()
        r = math.sqrt(x**2 + y**2 + z**2)
        lat = math.degrees(math.asin(z / r))
        lon = math.degrees(math.atan2(y, x))
        alt = r - EARTH_RADIUS
        return PolarCoordinate(lat, lon, alt)
