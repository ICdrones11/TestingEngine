#!/usr/bin/python
import math
from coordinate import *


def computeNextPolar(velocity, currentPolar):
    cartesian = currentPolar.toCartesian()
    cartesian = cartesian.nextLocation(velocity)
    return cartesian.toPolar()
