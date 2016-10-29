#!/usr/bin/python

import glob
import json

from Action import Action
from Drone import Drone
from TestCase import TestCase
from WayPointList import WayPointList


class TestCaseParser:
    def __init__(self, folderName):
        self.files = glob.glob('{}/*.json'.format(folderName))

    def parseAction(self, actionData):
        startTime = actionData["startTime"]
        act = actionData["action"]
        try:
            ttl = actionData["ttl"]
        except:
            ttl = None
        try:
            target = actionData["target"]
        except:
            target = None
        return Action(act, startTime, target, ttl)


    def parseDrone(self, droneData):
        startTime = int(droneData["startTime"])
        pointList = WayPointList(droneData["waypoints"])
        actionsList = droneData["actions"]
        actions = []
        for actionData in actionsList:
            actions.append(self.parseAction(actionData))
        return Drone(startTime, pointList, actions.sort())


    def parseDrones(self, droneList):
        drones = set()
        for droneData in droneList:
            drones.add(self.parseDrone(droneData))


    def load(self, fileName):
        fp = open(fileName, "r")
        jsonData = json.load(fp)
        name = jsonData["name"]
        timeLimit = int(jsonData["timeLimit"])
        droneList = jsonData["drones"]
        noFlyZones = jsonData["noFlyZones"]
        mannedAviation = jsonData["mannedAviation"]
        drones = self.parseDrones(droneList)
        testCase = TestCase(name, timeLimit, drones, noFlyZones, mannedAviation)
        return testCase


    def loadAll(self):
        testCases = set()
        for file in self.files:
            testCases.add(self.load(file))
        return testCases


def main():
    parser = TestCaseParser("droneData")
    testCases = parser.loadAll()


if __name__ == "__main__":
    main()
