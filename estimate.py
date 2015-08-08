#!/usr/bin/env python

import numpy as np
from math import sin, cos, tan, pi

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
    [0, 0, -1]
    ])

    # Ryaw_t = np.transpose(Ryaw)
    # Rpitch_t = np.transpose(Rpitch)
    # Rroll_t = np.transpose(Rroll)
    # Rcom_t = np.transpose(Rcom)

    IJK = mdot(Ryaw, Rpitch, Rroll)
    ENU = mdot(Rcom, IJK)

    E = mdot(np.array([1, 0, 0]), ENU)
    N = mdot(np.array([0, 1, 0]), ENU)
    U = mdot(np.array([0, 0, 1]), ENU)


    print("{}\n{}\n{}\n").format(E, N, U)


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
