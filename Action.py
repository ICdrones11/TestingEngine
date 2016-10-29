#!/usr/bin/python

class Action(object):
    MOVE = "move"
    LOSE_CONNECTION = "loseConnection"
    LAND = "land"

    def __init__(self, act, startTime, target = None, ttl = None):
        self.act = act
        self.target = target
        self.startTime = startTime
        self.target = target

    def __lt__(self, other):
        return self.startTime < other.startTime
