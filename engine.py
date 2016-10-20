#!/usr/bin/python
# The main test engine

import testCaseParser

from drone import *
from droneServerMessenger import *
from droneLogger import *

def main():
    drones = testCaseParser.getDrones("droneData/exampleDrone.json")
    messenger = DroneServerMessenger()
    logger = DroneLogger()

    # Log all drone initial positions and tell server of initial drone states
    for drone in drones:
    	logger.log(drone, 0)
    	drone.updateServer(messenger)

    duration = 10 # Simulation duration in time units
    for time in range(duration):
        for drone in drones:
            drone.tick(messenger)
            logger.log(drone, time + 1) # time + 1 so first movement is at t = 1
        messenger.notifyServerForTick()

    # Simulation finished, write logs to a file
    outputPath = "output/output.json"
    logger.save(outputPath)

if __name__ == "__main__":
    main()
