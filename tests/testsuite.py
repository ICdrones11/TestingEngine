#!/usr/bin/python

import sys
sys.path.append('/homes/dc3314/Desktop/GroupProject/TestEngine') 
# Adds upper directory to search path. TODO: Should NOT be hardcoded.

from droneJsonParser import *
from point import *
import unittest

droneTestCase = "/homes/dc3314/Desktop/GroupProject/" \
            "TestEngine/droneData/exampleDrone.data"

droneParser = DroneJsonParser(droneTestCase)

class TestDroneJsonParser(unittest.TestCase):

    def testLoadJsonFile(self):
        droneParser = DroneJsonParser(droneTestCase)
    
    @unittest.expectedFailure
    def testLoadNonExistingFile(self):
        nonExistingFile = 'null'
        DroneJsonParser(nonExistingFile)

    # We open a single parser with the example data for the
    # subsequent tests.   
    def testExtractFields(self):
        expectedStartPoint = Point(-21.14936, 123.64184, 1.15)
        actualStartPoint = droneParser.getStartPoint()
        self.assertEquals(expectedStartPoint, actualStartPoint)
        
        expectedEndPoint = Point(17.57878, -39.97062, 2.78)
        actualEndPoint = droneParser.getEndPoint()
        self.assertEquals(expectedEndPoint, actualEndPoint)

        expectedStartTime = 45
        actualStartTime = droneParser.getStartTime()
        self.assertEqual(expectedStartTime, actualStartTime)

        expectedEndTime = 75
        actualEndTime = droneParser.getEndTime()
        self.assertEqual(expectedEndTime, actualEndTime)


if __name__ == "__main__":
    unittest.main()

