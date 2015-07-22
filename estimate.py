#!/usr/bin/env python

import numpy as np
from math import sin, cos, pi

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

    # i think this one is wrong
    # rotation matrix from body frame to inertial frame
    Rcom = np.array([
    [cos(Compass), sin(Compass), 0],
    [-sin(Compass), cos(Compass), 0],
    [0, 0, -1]
    ])
    #print(Ryaw)
    #print(Rpitch)
    #print(Rroll)

    k = np.dot(np.array([0, 0, 1]), np.dot(Rroll, np.dot(Rpitch, np.dot(Ryaw,Rcom))))
    print('{0:.3f} N\n{1:.3f} E\n{2:.3f} z').format(k[0], k[1], k[2])


if __name__ == "__main__":
    yaw = 0
    pitch = 0
    roll = 0
    compass = 45
    estimate_wind(yaw, pitch, roll, compass)
