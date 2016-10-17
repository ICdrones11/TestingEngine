#!/usr/bin/python

from droneStatus import *
from droneServerMessenger import *
from vector import *
from gps import *

class Drone:
    # Initializes the drone with given droneInfo dictionnary.
    def __init__(self, did, startLocationVector, endLocationVector,
                startTime):        
        self.did = did
        self.velocityVector = Vector(0, 0, 0)
        self.startLocationVector = startLocationVector
        self.currentLocationVector = startLocationVector
        self.endLocationVector = endLocationVector
        self.startTime = startTime
        self.status = DroneStatus.HOVER # Initially, the drone is not moving.
        self.gps = Gps()

    # Defined to allow sorting of drones.
    def __lt__(self, other):
        return self.startTime < other.startTime
    
    # For debugging and representation purposes.
    def __str__(self):
        return "Drone with did {},\nMoving at:\n{} m/s on longitudinally,\n" \
               "{} m/s latitudinally,\n{} m/s upwards.".format(self.did, 
                self.velocityVector.x, self.velocityVector.y,
                self.velocityVector.z)
    

    # Get instructions from server.
    def getInstructions(self, messenger):
        instr= messenger.getInstructionsFromServer(self)
        self.processInstructions(instr)
    
    # Update the server with velocity, location and status.
    def updateServer(self, messenger):
        messenger.updateServer(self)

    # The function simulating the drone's CPU.
    def tick(self, messenger):
        self.updateServer(messenger)
        instr = self.getInstructions(messenger)
        self.processInstructions(instr)

    # Process instructions received from server.
    # For the moment just assumes the drone is allowed to move.
    def processInstructions(self, instr):
        desiredX = instr["desiredVelocity"]["x"]
        desiredY = instr["desiredVelocity"]["y"]
        desiredZ = instr["desiredVelocity"]["z"]
        desiredVelocityVector = Vector(desiredX, desiredY, desiredZ)
        currentLocationVector = self.gps.computeNextPolarLocation(
                                self.currentLocationVector,
                                desiredVelocityVector)
        print currentLocationVector
        return 0

    
