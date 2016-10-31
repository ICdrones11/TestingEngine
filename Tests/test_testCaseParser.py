import json
from unittest import TestCase

from DroneStatus import DroneStatus
from Action import Action
from PolarCoordinate import PolarCoordinate
from TestCaseParser import TestCaseParser
from Vector import Vector

parser = TestCaseParser("in/")

class TestTestCaseParser(TestCase):

    def test_findsFiles(self):
        self.assertEqual(len(parser.files), 6)

    def test_parseAction(self):
        fpMove = open("in/moveAction.json", "r")
        fpLand = open("in/landAction.json", "r")
        fpLose = open("in/loseConnectionAction.json", "r")

        moveJson = json.load(fpMove)
        loseJson = json.load(fpLose)
        landJson = json.load(fpLand)

        moveAction = parser.parseAction(moveJson)
        loseAction = parser.parseAction(loseJson)
        landAction = parser.parseAction(landJson)

        self.assertEqual(moveAction.act, Action.MOVE)
        self.assertEqual(moveAction.startTime, 2)
        self.assertNotEqual(moveAction.target, None)
        self.assertEqual(moveAction.ttl, 4)

        self.assertEqual(loseAction.act, Action.LOSE_CONNECTION)
        self.assertEqual(loseAction.startTime, 3)
        self.assertEqual(loseAction.target, None)
        self.assertEqual(loseAction.ttl, -1)

        self.assertEqual(landAction.act, Action.LAND)
        self.assertEqual(landAction.startTime, 5)
        self.assertEqual(landAction.target, None)
        self.assertEqual(landAction.ttl, None)

        fpLand.close()
        fpLose.close()
        fpMove.close()


    def test_parseDrone(self):
        fp = open("in/drone.json", "r")
        droneJson = json.load(fp)
        drone = parser.parseDrone(droneJson)

        self.assertEqual(drone.uid, "d1")
        self.assertEqual(drone.startTime, 1)
        self.assertEqual(len(drone.waypoints.pointList), 2)
        self.assertEqual(drone.velocity, Vector())

        posDict = { "lng" : 1.0, "lat" : 2.0, "alt" : 50.0 }
        expectedPolar = PolarCoordinate(*posDict.values())
        self.assertEqual(drone.polarPosition, expectedPolar)
        self.assertEqual(drone.velocity, Vector())
        self.assertEqual(drone.actionTtl, 0)
        self.assertEqual(drone.status, DroneStatus.HOVER)

        fp.close()


    def test_parseDrones(self):
        fp = open("in/drones.json", "r")
        dronesJson = json.load(fp)
        drones = parser.parseDrones(dronesJson)
        self.assertEqual(len(drones), 2)
        fp.close()

    def test_load(self):
        testCase = parser.load("in/exampleTestCase.json")
        self.assertEqual(testCase.name, "Test 1")
        self.assertEqual(testCase.timeLimit, 100)
        self.assertEqual(len(testCase.drones), 1)
        self.assertNotEqual(testCase.noFlyZones, None)
        self.assertNotEqual(testCase.mannedAviation, None)


    def test_loadAll(self):
        parser = TestCaseParser("in/testDirExample")
        testCases = parser.loadAll()
        self.assertEqual(len(testCases), 2)
