#!/usr/bin/python
# Wrapper around the REST API
import config
import requests
import json
from drone import *


class DroneServerMessenger:

    def __init__(self):
        baseAddress = config.SERVER_BASE_ADDR
        self.fullAddress = baseAddress + '/drone'
        self.tickingAddress = baseAddress + '/test'

    # A GET request to the API.
    def getInstructionsFromServer(self, drone):
        url = self.fullAddress + '/' + drone.did
        response = requests.get(url)
        data = json.loads(response.text)
        return data

    # Notify the server for an internal tick
    def notifyServerForTick(self):
        requests.get(self.tickingAddress)

    # Update the server using a PUT request.
    def updateServer(self, drone):
        headers = {'content-type': 'application/json'}
        startPolar = drone.startPolar
        endPolar = drone.endPolar
        vel = drone.velocityVector
        currentPolar = drone.currentPolar
        payload = {
            'uid':
                drone.did,
            'startPoint': {
                'x': startPolar.lat,
                'y': startPolar.lon,
                'z': startPolar.alt
            },
            'endPoint': {
                'x': endPolar.lat,
                'y': endPolar.lon,
                'z': endPolar.alt
            },
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
            'status':
                drone.status
        }
        url = self.fullAddress + '/' + drone.did
        response = requests.put(url, data=json.dumps(payload), headers=headers)
