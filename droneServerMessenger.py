#!/usr/bin/python
# Wrapper around the REST API

import requests
import urllib
import urllib2
import json
from drone import *

class DroneServerMessenger:
    def __init__(self):
        # Hardcoded server address.
        self.serverAddress = "http://dronesservice.azurewebsites.net/api/drone"

    # An UPDATE request to the API.
    def updateServer(self, drone):
        return 0

    # A GET request to the API.
    def getMetricsFromServer(self):
        response = urllib2.urlopen(self.serverAddress)
        data = json.load(response) 
        return data

    # A POST request to the API.
    # Creates a POST request given a list of drones.
    def postRequestToServer(self, drones):
       payload = []
       for drone in drones:
           payload.append(computeDronePayload(drone))
       response = requests.post(self.serverAddress, data=json.dumps(payload), 
                    headers=headers) 


    def computeDronePayLoad(drone):
        sp = drone.startLocationVector
        ep = drone.endLocationVector
        dronePayload = {'uid': drone.did,
                  'startPoint' : {'x':sp[0], 'y':sp[1], 'z':sp[2]}, 
                   'endPoint' : {'x':ep[0], 'y':ep[1], 'z':ep[2]}} 
        return dronePayload
	
