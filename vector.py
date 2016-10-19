#!/usr/bin/python


class Vector:

    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z

    def __add__(self, other):
        x = self.x + other.x
        y = self.y + other.y
        z = self.z + other.z
        return Vector(x, y, z)

    def unbox(self):
        return self.x, self.y, self.z

    def __str__(self):
        return 'Vector: [{}, {}, {}]'.format(self.x, self.y, self.z)
