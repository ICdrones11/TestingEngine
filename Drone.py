#!/usr/bin/python
import PositionConversions
from Action import Action
from Logger import Logger
from DroneStatus import *
from PolarCoordinate import PolarCoordinate
from ServerMessenger import *
from Vector import Vector


class Drone:
    def __init__(self, uid, startTime, waypoints, actions):
        self.uid = uid
        self.startTime = startTime
        self.waypoints = waypoints
        self.actions = actions # Actions are sorted
        self.logger = Logger()
        assert waypoints
        self.polarPosition = PolarCoordinate(*waypoints.pointList[0].values())
        self.velocity = Vector()
        self.actionTtl = 0
        self.status = DroneStatus.HOVER

    def getLogger(self):
        return self.logger

    def land(self):
        self.status = DroneStatus.LAND
        self.velocity = Vector(0, 0, -5)

    def move(self):
        pass
        #self.polarPosition = PositionConversions.nextPolar(self.polarPosition, self.velocity)
        #print self.polarPosition


    def log(self):
        pass


    def tick(self, time, messenger):
        messenger.updateServer(self)
        instructions = messenger.getInstructionsFromServer(self)
        #
        #
        # if self.actionTtl != 0:
        #     # The drone is carrying out an action.
        #     pass
        # elif self.actions and self.actions[0].startTime == time:
        #     action = self.actions.pop(0)
        #
        #     # run the action.
        # else:
        #     pass
        #     # run the instruction
        # messenger.notifyServerForTick()

