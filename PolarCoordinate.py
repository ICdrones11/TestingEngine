#!/usr/bin/python
from Vector import Vector


class PolarCoordinate:
    def __init__(self, lat, lng, alt):
        self.position = Vector(lat, lng, alt)

    @property
    def lat(self):
        return self.position.x

    @property
    def lon(self):
        return self.position.y

    @property
    def alt(self):
        return self.position.z

    def unbox(self):
        return self.position.unbox()

    def __eq__(self, other):
        return self.position == other.position

    def __str__(self):
        return str(self.position)
