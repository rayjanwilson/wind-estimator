#!/usr/bin/env python
from __future__ import print_function
from __future__ import division
import time

UNIX2GPS = 315964800    # seconds from UNIX to GPS epoch
GPS_LEAP_SECONDS = 17   # leap seconds since GPS epoch (as of 8/5/2015)
                        # http://tycho.usno.navy.mil/leapsec.html

def gps_to_human(gpstime):
    unixtime = int(gpstime) + UNIX2GPS - GPS_LEAP_SECONDS
    gmtime = time.gmtime(int(unixtime))
    return time.strftime("%a %b %d %H:%M:%S %Y GMT", gmtime)


def toGPSTime(gps_week_ms, gps_week_number):
    return (int(gps_week_ms/1000) + (gps_week_number * 60 * 60 * 24 * 7))

if __name__ == '__main__':
    print("GPS Week: ", 1853)
    print("GPS Week Seconds: ", 501201000)
    gps_time = toGPSTime(501201000, 1853)
    human_time = gps_to_human(gps_time)
    print(human_time)
