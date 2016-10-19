#!/usr/bin/python
import json

class DroneLogger:

    def __init__():
        self.drones = {}
        pass

    def log(drone, timeUnit):
        uid = drone.did
        polar = drone.currentLocationVector
        timeUnit = timeUnit
        if (self.drones[uid] == None):
            self.drones[uid] = {
                uid: uid,
                waypoints: []
            }

        self.drones[uid].waypoints.append({
            lat: polar.lat,
            lon: polar.lon,
            alt: polar.alt,
            timestamp: timeUnit
        })

    # saves the current info as a JSON file in spe
    def save(outputPath):
        outfile = open(outputPath, 'w+')
        output = getListRepresentation()
        json.dump(output, output)

    # Converts drone dictionary into list
    def getListRepresentation():
        res = []
        for uid, drone in self.drones.iteritems():
            res.append({
                uid: uid,
                waypoints: drone.waypoints
            })

        return  res
