#!/usr/bin/python
import gps
from vector import *

'''
Given start and end points in LLA format and a journey duration (in arb. time units),
this program gives back the velocity in m/timeUnit a drone would have
at in order to complete the journey on time.
'''
startMessage = """Given start and end points in LLA format and a journey duration (in arb. time units),
this program gives back the velocity in m/timeUnit a drone would have
at in order to complete the journey on time."""

def calcJourneyVelocity(startPolar, endPolar, journeyDuration):
    startX, startY, startZ = gps.computeTerrestrialCoordinates(startPolar).unbox()
    endX, endY, endZ = gps.computeTerrestrialCoordinates(endPolar).unbox()

    vx = (endX - startX) / journeyDuration
    vy = (endY - startY) / journeyDuration
    vz = (endZ - startZ) / journeyDuration
    return Vector(
            vx,
            vy,
            vz
            )

def getPolarInput():
    lat = input("Enter latitude: ")
    lon = input("Enter longitude: ")
    alt = input("Enter altitude: ")
    return Vector(lon, lat, alt)


def getJourneyDurationInput():
    return input("")

def main():
    # Prompt user for inputs
    print("")
    print(startMessage)
    print("")

    print("Start Position:")
    startPolar = getPolarInput()
    print("")

    print("End Position:")
    endPolar = getPolarInput()
    print("")

    print("Journey duration in arb. time units: ")
    journeyDuration = getJourneyDurationInput()
    print("")

    print("Required velocity in m/timeUnit is:")
    print(calcJourneyVelocity(startPolar, endPolar, journeyDuration))


if __name__ == "__main__":
    main()