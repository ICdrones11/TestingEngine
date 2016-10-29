#!/usr/bin/python
import Config
import requests
import json
from Drone import *


class ServerMessenger:
    def __init__(self):
        baseAddress = Config.SERVER_BASE_ADDR
        self.fullAddress = baseAddress + '/drone'
        self.tickingAddress = baseAddress + '/test'

    def getInstructionsFromServer(self, drone):
        url = self.fullAddress + '/' + drone.uid
        response = requests.get(url)
        data = json.loads(response.text)
        return data

    def notifyServerForTick(self):
        requests.get(self.tickingAddress)


    def postTestCase(self, noFlyZones, mannedAviation):
        pass


    # Update the server using a PUT request.
    def updateServer(self, drone):
        headers = {'content-type': 'application/json'}
        vel = drone.velocityVector
        currentPolar = drone.polarPosition
        payload = {
        'uid':drone.did,
        'velocity': {
            'x': vel.x,
            'y': vel.y,
            'z': vel.z
        },
        'position': {
            'x': currentPolar.lat,
            'y': currentPolar.lon,
            'z': currentPolar.alt
        },
        'status':drone.status,
        'waypoints': drone.waypoints
        }

        url = self.fullAddress + '/' + drone.did
        response = requests.put(url, data=json.dumps(payload), headers=headers)

