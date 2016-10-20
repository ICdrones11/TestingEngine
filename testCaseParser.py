#!/usr/bin/python

from drone import *
from vector import *
from coordinate import *
import json


# Returns a set of drones created from the JSON file.
def getDrones(filename):
    fp = open(filename, "r")
    jsonData = json.load(fp)
    droneList = []
    for droneDictionnary in jsonData["drones"]:
        droneList.append(createDroneFromDictionnary(droneDictionnary))
    droneList.sort()
    return droneList


# Parses the dictionnary, and returns a drone from it.
def createDroneFromDictionnary(droneInfo):
    did = droneInfo["did"]
    startLon = droneInfo["start_point"]["longitude"]
    startLat = droneInfo["start_point"]["latitude"]
    startAlt = droneInfo["start_point"]["altitude"]
    endLon = droneInfo["end_point"]["longitude"]
    endLat = droneInfo["end_point"]["latitude"]
    endAlt = droneInfo["end_point"]["altitude"]
    startPolar = PolarCoordinate(startLat, startLon, startAlt)
    endPolar = PolarCoordinate(endLat, endLon, endAlt)
    startTime = droneInfo["start_time"]
    return Drone(did, startPolar, endPolar, startTime)
