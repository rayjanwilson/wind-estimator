#!/usr/bin/env python

import numpy as np
from math import sin, cos, pi

Yaw = 0
Pitch = 0
Roll = 0
Compass = 45

Yaw = Yaw * pi/180
Pitch = Pitch * pi/180
Roll = Roll * pi/180
Compass = Compass * pi/180

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
#print(Ryaw)
#print(Rpitch)
#print(Rroll)

k = np.dot(np.array([0, 0, 1]), np.dot(Rroll, np.dot(Rpitch, np.dot(Ryaw,Rcom))))
print('{0:.3f} N\n{1:.3f} E\n{2:.3f} z').format(k[0], k[1], k[2])
