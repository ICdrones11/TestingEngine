#!/usr/bin/python
import json

import DroneStatus


class Logger:
    def __init__(self):
        self.text = []

    def record(self, str):
        self.text.append(str)


class DroneLogger(Logger):

    def __init__(self, uid, drone):
        self.uid = uid
        self.actions = []
        self.drone = drone

    def log(self, timestamp):
        action = {"action": self.drone.status, "timestamp": timestamp}
        if self.drone.status == "MOVE":
            action["lng"] = self.drone.polarPosition.lng
            action["lat"] = self.drone.polarPosition.lat
            action["alt"] = self.drone.polarPosition.alt
        self.actions.append(action)

    def generateLog(self):
        log = {"id": self.uid, "waypoints": self.actions}
        return json.dumps(log)









