#!/usr/bin/python

from droneStatus import *
from droneServerMessenger import *
from vector import *
import gps


class Drone:
    # Initializes the drone with given droneInfo dictionnary.
    def __init__(self, did, startPolar, endPolar, startTime):
        self.did = did
        # Velocity vector hardcoded so that we go from SK to Hammersmith in 10 ticks 
        self.velocityVector = Vector(-219.797336281772 / 10,
                                     -4264.274850190377 / 10,
                                     257.61475772469566 / 10)
        self.startPolar = startPolar
        self.currentPolar = startPolar
        self.endPolar = endPolar
        self.startTime = startTime
        self.status = DroneStatus.HOVER  # Initially, the drone is not moving.

    # Defined to allow sorting of drones.
    def __lt__(self, other):
        return self.startTime < other.startTime

    # Get instructions from server.
    def getInstructions(self, messenger):
        instr = messenger.getInstructionsFromServer(self)
        self.processInstructions(instr)

    # Update the server with velocity, location and status.
    def updateServer(self, messenger):
        messenger.updateServer(self)

    # The function simulating the drone's CPU.
    def tick(self, messenger):
        #instr = self.getInstructions(messenger)
        #self.processInstructions(instr)
        self.computeNextLocation()
        self.updateServer(messenger)

    def computeNextLocation(self):
        self.currentPolar = gps.computeNextPolar(self.velocityVector,
                                                 self.currentPolar)

    # Process instructions received from server.
    # For the moment just assumes the drone is allowed to move.
    def processInstructions(self, instr):
        desiredX = instr["desiredVelocity"]["x"]
        desiredY = instr["desiredVelocity"]["y"]
        desiredZ = instr["desiredVelocity"]["z"]
        desiredVelocityVector = Vector(desiredX, desiredY, desiredZ)
        currentLocationVector = gps.computeNextPolarLocation(
            desiredVelocityVector, self.currentLocationVector)
