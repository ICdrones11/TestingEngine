#!/usr/bin/python

from droneServerMessenger import *

class Drone:
    # Initializes the drone with given droneInfo dictionnary.
    def __init__(self, did, startLocationVector, endLocationVector,
                startTime):        
        self.did = did
        self.velocityVector = [0, 0, 0]
        self.startLocationVector = startLocationVector
        self.endLocationVector = endLocationVector
        self.startTime = startTime

    # Defined to allow sorting of drones.
    def __lt__(self, other):
        return self.startTime < other.startTime
    
    # For debugging and representation purposes.
    def __str__(self):
        return "Drone with did {},\nMoving at:\n{} m/s on longitudinally,\n" \
               "{} m/s latitudinally,\n{} m/s upwards.".format(self.did, 
                self.velocityVector[0], self.velocityVector[1],
                self.velocityVector[2])
    
    # The function simulating the drone's CPU.
    def tick(self, instructions):
        return 0
        # Updates the server.
        # Pulls information from the server
        # Recomputes the next location, sets the new values.


