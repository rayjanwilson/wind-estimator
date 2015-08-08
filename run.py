#!/usr/bin/env python
from __future__ import print_function
from __future__ import division
from DataflashLog import DataflashLog, LogIterator, DataflashLogHelper
import collections
import gps_to_human_time as gps

logfile = "logs/15-07-17_11-29-32.log"
#logfile = "logs/15-07-17_11-57-40.log"
print("Parsing: ", logfile)
logdata = DataflashLog(logfile)
print("Complete")

#print("GPS Labels: ", logdata.formats['GPS'].labels)
#print("ATT Labels: ", logdata.formats['ATT'].labels)
#print("EKF1 Labels: ", logdata.formats['EKF1'].labels)
print("Duration [s]: ", logdata.durationSecs)

loiterChunks = DataflashLogHelper.findLoiterChunks(logdata)
print("Number of loiters: ", len(loiterChunks))
print(loiterChunks)


# ignore anything below this altitude, to discard any data while not flying
minAltThreshold = 1.5 # meters

for (startLine,endLine) in loiterChunks:
    lit = LogIterator(logdata, startLine)
    assert(lit.currentLine == startLine)
    gpsStart = lit["GPS"]["GMS"]
    increment = 1000
    nextgpsTime = gpsStart + increment
    print("GPS Start: ", gpsStart)
    i=0
    print("i", "lit.currentLine", "timeUS", "timeGPS_GMS", "timeGPS_GWk", "timeGPS_DaySec", "roll", "pitch", "yaw", "vd", "pd", "lat", "lon")
    while lit.currentLine <= endLine:
        if (nextgpsTime <= lit["GPS"]["GMS"]):
            # only parse the log every gps second
            timeUS = lit["GPS"]["TimeUS"]
            timeGPS_GMS = lit["GPS"]["GMS"]
            timeGPS_GWk = lit["GPS"]["GWk"]
            timeGPS_DaySec = gps.weekMS_to_daySec(timeGPS_GMS, timeGPS_GWk)
            roll  = lit["EKF1"]["Roll"]
            pitch = lit["EKF1"]["Pitch"]
            yaw = lit["EKF1"]["Yaw"]
            vd = lit["EKF1"]["VD"]
            pd = lit["EKF1"]["PD"]
            lat = lit["GPS"]["Lat"]
            lon = lit["GPS"]["Lng"]

            print(i, lit.currentLine, timeUS, timeGPS_GMS, timeGPS_GWk, timeGPS_DaySec, roll, pitch, yaw, vd, pd, lat, lon)

            nextgpsTime = nextgpsTime + increment
            i += 1
        lit.next()

# really want to loop through the log by gps seconds
# either record the line number, or do a snapshot when the gps has reached the next second
# and then do a snapshot for each
#

# hovering = (lit["EKF1"]["VD"] < 0.2) and (lit["EKF1"]["VE"] < 0.2) and (lit["EKF1"]["VN"] < 0.2)
# hovering = (lit["EKF1"]["VD"] > -0.2) and (lit["EKF1"]["VE"] > -0.2) and (lit["EKF1"]["VN"] > -0.2) and hovering
# goodGPS = (lit["GPS"]["Status"] == 3)
# aboveMinHeight = (lit["EKF1"]["PD"] < -1*minAltThreshold)
#if (goodGPS and hovering and aboveMinHeight):
# timeUS = lit["GPS"]["TimeUS"]
# timeGPS = lit["GPS"]["GMS"]
# roll  = lit["EKF1"]["Roll"]
# pitch = lit["EKF1"]["Pitch"]
# yaw = lit["EKF1"]["Yaw"]
# vd = lit["EKF1"]["VD"]
# pd = lit["EKF1"]["PD"]
# lat = lit["GPS"]["Lat"]
# lon = lit["GPS"]["Lng"]
