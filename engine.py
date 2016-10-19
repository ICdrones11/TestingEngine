#!/usr/bin/python
# The main test engine

from drone import *
from droneServerMessenger import *
import testCaseParser


def main():
    drones = testCaseParser.getDrones("/homes/dc3314/Desktop/GroupProject/" \
                        "TestEngine/droneData/exampleDrone.data")
    messenger = DroneServerMessenger()
    #    # Initialization.
    #    for drone in drones:
    #        messenger.postDroneRequestToServer(drone)

    for drone in drones:
        drone.getInstructions(messenger)


if __name__ == "__main__":
    main()
