#!/usr/bin/env python

from __future__ import division
import numpy as np
import numpy.linalg as la
from math import sin, cos, tan, pi

def ang(v1, v2):
    """ Returns the angle in radians between vectors 'v1' and 'v2'    """
    cosang = np.dot(v1, v2)
    sinang = la.norm(np.cross(v1, v2))
    return np.arctan2(sinang, cosang)

def mdot(*args):
    return reduce(np.dot, args)

def estimate_wind(yaw=0, pitch=0, roll=0, compass=0):
    Yaw = yaw * pi/180
    Pitch = pitch * pi/180
    Roll = roll * pi/180
    Compass = compass * pi/180

    Ryaw = np.array([
    [cos(Yaw), sin(Yaw), 0],
    [-sin(Yaw), cos(Yaw), 0],
    [0, 0, 1]
    ])
    Rpitch = np.array([
    [cos(Pitch), 0, -sin(Pitch)],
    [0, 1, 0],
    [sin(Pitch), 0, cos(Pitch)]
    ])
    Rroll = np.array([
    [1, 0, 0],
    [0, cos(Roll), sin(Roll)],
    [0, -sin(Roll), cos(Roll)]
    ])
    Rcom = np.array([
    [cos(Compass), sin(Compass), 0],
    [-sin(Compass), cos(Compass), 0],
    [0, 0, 1]
    ])

    # Ryaw_t = np.transpose(Ryaw)
    # Rpitch_t = np.transpose(Rpitch)
    # Rroll_t = np.transpose(Rroll)
    # Rcom_t = np.transpose(Rcom)

    ijk = mdot(Ryaw, Rpitch, Rroll) # in terms of IJK
    print("ijk:\n{}").format(ijk)
    ijkENU = mdot(Rcom, ijk) # in terms of ENU
    print("ijkENU\n{}").format(ijkENU)

    iENU = mdot(np.array([1, 0, 0]), ijkENU)
    jENU = mdot(np.array([0, 1, 0]), ijkENU)
    kENU = mdot(np.array([0, 0, 1]), ijkENU)

    k_unit = np.linalg.norm(kENU)
    print("kENU {}").format(kENU)
    U = np.array([0, 0, 1])

    tiltAngle = ang(kENU, U) * 180/pi
    print("tilt: {}\n\n").format(tiltAngle)


if __name__ == "__main__":
    yaw = 0
    pitch = 0
    roll = 0
    compass = 0

    print("zeros")
    estimate_wind(yaw, pitch, roll, compass)
    print("compass 45, no rotation")
    estimate_wind(yaw, pitch, roll, 45)
    print("yaw 45, compass 45")
    estimate_wind(45, pitch, roll, 45)
    print("compass small angle")
    estimate_wind(yaw, pitch, roll, 1)
    print("compass 0, pitch 45")
    estimate_wind(0, 45, 0, 0)
