#!/usr/bin/python
# Wrapper around the REST API

import requests
import json
from drone import *


class DroneServerMessenger:
    def __init__(self):
        self.baseAddress = 'http://dronesservice.azurewebsites.net/api'
        self.fullAddress = self.baseAddress + '/drone'
        self.tickingAddress = self.baseAddress + '/test'

    # A GET request to the API.
    def getInstructionsFromServer(self, drone):
        url = self.fullAddress + '/' + drone.did
        print url
        response = requests.get(url)
        data = json.loads(response.text)
        return data

    # A POST request for the API, given a drone.
    def postDroneRequestToServer(self, drone):
        headers = {'content-type': 'application/json'}
        response = requests.post(self.fullAddress, 
                                data=json.dumps(self.computeDronePayload(drone)), 
                                headers=headers) 
        
    # Notify the server for an internal tick
    def notifyServerForTick(self):
        requests.get(self.tickingAddress)

    # Update the server using a PUT request.
    def updateServer(self, drone):
        headers = {'content-type': 'application/json'}
        vel = drone.velocityVector
        loc = drone.currentLocationVector
        payload = {'ActualVelocity': {'x':vel.x,'y':vel.y,'z':vel.z},
                    'Position':{'x':loc.x,'y':loc.y,'z':loc.z}, 
                    'currentstatus':drone.status}
        url = self.fullAddress + '/' + drone.did
        response = requests.put(url, data=json.dumps(payload), headers=headers)

    # Private helper function.
    def computeDronePayload(self, drone):
        sl = drone.startLocationVector
        el = drone.endLocationVector
        dronePayload = {'uid': drone.did,
                        'startPoint' : {'x':sl.x, 'y':sl.y, 'z':sl.z}, 
                        'endPoint' : {'x':el.x, 'y':el.y, 'z':el.z}} 
        return dronePayload


