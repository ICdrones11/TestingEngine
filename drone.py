#!/usr/bin/python

from serverMessenger import *

class Drone:
    # Initializes the drone with given droneInfo dictionnary.
    def __init__(self, did, startLocationVector, endLocationVector,
                startTime):        
        self.did = did
        self.velocityVector = [0, 0, 0]
        self.startlocationVector = startLocationVector
        self.endlocationVector = endLocationVector
        self.startTime = startTime
        self.serverMessenger = ServerMessenger()

    def __lt__(self, other):
        return self.startTime < other.startTime

    def tick(self, sender):
        return 0
        
        # Updates the server.
        # Pulls information from the server
        # Recomputes the next location, sets the new values.


