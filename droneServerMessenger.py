#!/usr/bin/python
# Wrapper around the REST API

import requests
import json
from drone import *


class DroneServerMessenger:

    def __init__(self):
        self.baseAddress = 'http://localhost:5000/api' #'http://dronesservice.azurewebsites.net/api'
        self.fullAddress = self.baseAddress + '/drone'
        self.tickingAddress = self.baseAddress + '/test'

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
        sl = drone.startLocationVector
        el = drone.endLocationVector
        vel = drone.velocityVector
        loc = drone.currentLocationVector
        print(loc)
        payload = {
            'uid': drone.did,
            'startPoint': {
                'x': sl.x,
                'y': sl.y,
                'z': sl.z
            },
            'endPoint': {
                'x': el.x,
                'y': el.y,
                'z': el.z
            },
            'velocity': {
                'x': vel.x,
                'y': vel.y,
                'z': vel.z
            },
            'position': {
                'x': loc.x,
                'y': loc.y,
                'z': loc.z
            },
            'status': drone.status
        }
        url = self.fullAddress + '/' + drone.did
        response = requests.put(url, data=json.dumps(payload), headers=headers)
