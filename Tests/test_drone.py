from unittest import TestCase

from DroneStatus import DroneStatus
from TestCaseParser import TestCaseParser
import json

from Vector import Vector

parser = TestCaseParser("")
actionJson = json.load(open("in/drone.json", "r"))
drone = parser.parseDrone(actionJson)

class TestDrone(TestCase):

    def test_getLogger(self):
        self.assertNotEqual(drone.getLogger(), None)

    def test_land(self):
        self.assertEqual(drone.status, DroneStatus.HOVER)
        drone.land()
        self.assertEqual(drone.status, DroneStatus.LAND)
        self.assertEqual(drone.velocity, Vector(0, 0, -5))

    def test_move(self):
        self.fail()
        # drone.velocity = Vector(5, 5, 0)
        # drone.move()


    def test_log(self):
        self.fail()


    def test_execute(self):
        self.fail()

    def test_tick(self):
        self.fail()
