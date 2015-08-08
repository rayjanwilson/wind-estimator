#!/usr/bin/env python

import numpy as np
import matplotlib.pyplot as plt

wind_data=np.genfromtxt('logs/u_v_w.txt',usecols = (0, 1, 2, 3), names=['time', 'u', 'v', 'w'], autostrip=True)
drone_data=np.genfromtxt('logs/state-sample-29-32.txt',usecols = (5, 6, 7, 8, 9, 10), names=['time', 'roll', 'pitch', 'yaw', 'vd', 'pd'], autostrip=True)
plt.plot(drone_data['time'], -1*drone_data['pd'])
plt.show()
