#!/usr/bin/python
from DroneException import DroneException
from ServerMessenger import ServerMessenger


class TestCase:
    def __init__(self, name, timeLimit, drones, noFlyZones, mannedAviation):
        self.name = name
        self.timeLimit = timeLimit
        self.drones = drones
        self.noFlyZones = noFlyZones
        self.mannedAviation = mannedAviation
        self.serverMessenger = ServerMessenger()


    def run(self):
        self.serverMessenger.postTestCase(self.noFlyZones, self.mannedAviation)
        i = 0
        while i < self.timeLimit:
            for drone in self.drones:
                try:
                    drone.tick(i, self.serverMessenger)
                except DroneException:
                    return False
            i += 1
        return 0

