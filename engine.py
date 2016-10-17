#!/usr/bin/python
# The main test engine

from drone import *
from droneServerMessenger import *
from testCaseParser import *



def main():
    t = TestCaseParser("/homes/dc3314/Desktop/GroupProject/" \
                        "TestEngine/droneData/exampleDrone.data")
    drones = t.getDrones()
    messenger = DroneServerMessenger()
#    # Initialization.
#    for drone in drones:
#        messenger.postDroneRequestToServer(drone)

    for drone in drones:
        drone.getInstructions(messenger)
    

if __name__ == "__main__":
    main()


