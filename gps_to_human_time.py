#!/usr/bin/env python
from __future__ import print_function
from __future__ import division
import time

def toUnixTime(gpstime):
    UNIX2GPS = 315964800    # seconds from UNIX to GPS epoch
    GPS_LEAP_SECONDS = 17   # leap seconds since GPS epoch (as of 8/5/2015)
                            # http://tycho.usno.navy.mil/leapsec.html
    return int(gpstime) + UNIX2GPS - GPS_LEAP_SECONDS

def gps_to_human(gpstime):
    gmtime = time.gmtime(toUnixTime(gpstime))
    return time.strftime("%a %b %d %H:%M:%S %Y GMT", gmtime)


def toGPSTime(gps_week_ms, gps_week_number):
    return (int(gps_week_ms/1000) + (gps_week_number * 60 * 60 * 24 * 7))

def toTimeObj(gps_week_ms, gps_week_number):
    unixtime = toUnixTime(toGPSTime(gps_week_ms, gps_week_number))
    return time.gmtime(unixtime)

def weekMS_to_daySec(gps_week_ms, gps_week_number):
    t1 = toTimeObj(gps_week_ms, gps_week_number)
    day_sec = t1.tm_sec + t1.tm_min*60 + t1.tm_hour*60*60
    return day_sec

if __name__ == '__main__':
    print("GPS Week: ", 1853)
    print("GPS Week Seconds: ", 501202800)
    gps_time = toGPSTime(501202800, 1853)
    human_time = gps_to_human(gps_time)

    print(human_time)
    
    print(weekMS_to_daySec(501202800, 1853))
    print(toTimeObj(501202800, 1853))
