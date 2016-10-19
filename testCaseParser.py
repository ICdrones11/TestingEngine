#!/usr/bin/python

from drone import *
from vector import *
import vector
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
    startX = droneInfo["start_point"]["longitude"]
    startY = droneInfo["start_point"]["latitude"]
    startZ = droneInfo["start_point"]["altitude"]
    startLocationVector = Vector(startX, startY, startZ)
    endX = droneInfo["end_point"]["longitude"]
    endY = droneInfo["end_point"]["latitude"]
    endZ = droneInfo["end_point"]["altitude"]
    endLocationVector = Vector(endX, endY, endZ)
    startTime = droneInfo["start_time"]
    return Drone(did, startLocationVector, endLocationVector, startTime)
