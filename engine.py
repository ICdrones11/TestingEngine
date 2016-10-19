#!/usr/bin/python
# The main test engine

from drone import *
from droneServerMessenger import *
import testCaseParser


def main():
    drones = testCaseParser.getDrones("droneData/exampleDrone.json")
    messenger = DroneServerMessenger()
    for i in range(10):
        for drone in drones:
            drone.tick(messenger)
        messenger.notifyServerForTick()


if __name__ == "__main__":
    main()
