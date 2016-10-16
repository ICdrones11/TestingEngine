#!/usr/bin/python

from drone import *
import json

# Class intented to parse a .data testcase file.
class TestCaseParser:
    def __init__(self, filename):
        self.fp = open(filename, "r")
        self.jsonData = json.load(self.fp)

    # Returns a set of drones created from the JSON file.
    def getDrones(self):
        droneSet = []
        for droneDictionnary in self.jsonData["drones"]:
            droneSet.append(self.createDroneFromDictionnary(droneDictionnary))
        droneSet.sort()
        return droneSet

    # Parses the dictionnary, and returns a drone from it.
    def createDroneFromDictionnary(self, droneInfo):
        did = droneInfo["did"]
        startX = droneInfo["start_point"]["longitude"]
        startY = droneInfo["start_point"]["latitude"]
        startZ = droneInfo["start_point"]["altitude"]
        startLocationVector = [startX, startY, startZ]
        endX = droneInfo["end_point"]["longitude"]
        endY = droneInfo["end_point"]["latitude"]
        endZ = droneInfo["end_point"]["altitude"]
        endLocationVector = [endX, endY, endZ]
        startTime = droneInfo["start_time"]
        return Drone(did, startLocationVector, endLocationVector, startTime)

def main():
    t = TestCaseParser("/homes/dc3314/Desktop/GroupProject/TestEngine/droneData/exampleDrone.data")
    s = t.getDrones()
    print s

if __name__ == "__main__":
    main()
