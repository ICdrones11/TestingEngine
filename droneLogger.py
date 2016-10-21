#!/usr/bin/python
import json


class DroneLogger:

    def __init__(self):
        self.drones = {}

    def log(self, drone, timeUnit):
        uid = drone.did
        lat, lon, alt = drone.currentPolar.unbox()
        if (not (uid in self.drones)):
            self.drones[uid] = {'uid': uid, 'waypoints': []}

#        print '{}, {}, {}'.format(lat, lon, alt) 
        self.drones[uid]['waypoints'].append({
            'lat': lat,
            'lon': lon,
            'alt': alt,
            'timestamp': timeUnit
        })

    # saves the current info as a JSON file in spe
    def save(self, outputPath):
        outfile = open(outputPath, 'w+')
        output = self.getListRepresentation()
        json.dump(output, outfile)

    # Converts drone dictionary into list
    def getListRepresentation(self):
        res = []
        for uid, drone in self.drones.iteritems():
            res.append(drone)
        return res
