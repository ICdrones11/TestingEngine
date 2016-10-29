#!/usr/bin/python
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
        self.polarPosition = PolarCoordinate(*waypoints[0].values())
        self.velocity = Vector()
        self.ttl = 0

    def initialize(self):
        pass

    def getLogger(self):
        return self.logger

    def land(self):
        pass

    def move(self):
        pass

    def log(self):
        pass

    def continueMove(self):
        pass


    def execute(self, action):
        act = action.act
        self.ttl = action.ttl
        if act == Action.MOVE:
            self.move()
        if act == Action.LAND:
          self.land()
        if act == Action.LOSE_CONNECTION:
            self.continueMove()


    def tick(self, time, messenger):
        messenger.updateServer(self)
        instructions = messenger.getInstructionsFromServer(self)
        if time == self.startTime:
            self.initialize()
        if self.ttl != 0:
            # The drone is carrying out an action.
            pass
        elif self.actions and self.actions[0].startTime == time:
            action = self.actions.pop(0)
            self.execute(action)
            # run the action.
        else:
            pass
            # run the instruction
        messenger.notifyServerForTick()

