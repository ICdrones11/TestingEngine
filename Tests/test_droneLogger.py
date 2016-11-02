from unittest import TestCase

from DroneStatus import DroneStatus
from TestCaseParser import TestCaseParser
from Drone import Drone
import json

from Vector import Vector

parser = TestCaseParser("")
actionJson = json.load(open("in/drone.json", "r"))
drone = parser.parseDrone(actionJson)

class TestDroneLogger(TestCase):

    def test_droneLoggerEmptyLog(self):
        fp = open("in/drones.json", "r")
        dronesJson = json.load(fp)
        log = drone.logger.generateLog()
        fp = open("out/emptyDrone.json", "r")

        self.assertEqual(json.loads(log), json.load(fp))


    def test_droneLoggerMoveLog(self):
        fp = open("in/drones.json", "r")
        dronesJson = json.load(fp)
        drone.status = "MOVE"

        drone.log()
        log = drone.logger.generateLog()

        fp = open("out/droneWithMove.json", "r")

        self.assertEqual(json.loads(log), json.load(fp))

