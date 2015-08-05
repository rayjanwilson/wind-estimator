#!/usr/bin/env python
from __future__ import print_function
from __future__ import division
import DataFlash as DataflashLog
import collections

logfile = "logs/15-07-17_11-29-32.log"
logdata = DataflashLog.DataflashLog()
print("Parsing: ", logfile)
logdata.read(logfile, ignoreBadlines=True)
print("Complete")

print("GPS Labels: ", logdata.formats['GPS'].labels)
print("ATT Labels: ", logdata.formats['ATT'].labels)
print("EKF1 Labels: ", logdata.formats['EKF1'].labels)
print("Duration [s]: ", logdata.durationSecs)

lit = DataflashLog.LogIterator(logdata)
#print("lit current line: ", lit.currentLine)
#print("lit iterators: ", lit.iterators)

# figure out where the Loiter modes begin and end
# https://github.com/diydrones/ardupilot/blob/master/Tools/LogAnalyzer/tests/TestPitchRollCoupling.py#L29
autoModes   = ["RTL","AUTO","LAND","LOITER","GUIDED","CIRCLE","OF_LOITER","HYBRID"]     # use NTUN DRol+DPit
manualModes = ["STABILIZE","DRIFT","ALTHOLD","ALT_HOLD","POSHOLD"]                      # use CTUN RollIn/DesRoll + PitchIn/DesPitch
ignoreModes = ["ACRO","SPORT","FLIP","AUTOTUNE",""]                            # ignore data from these modes
autoSegments   = []  # list of (startLine,endLine) pairs
manualSegments = []  # list of (startLine,endLine) pairs
orderedModes = collections.OrderedDict(sorted(logdata.modeChanges.items(), key=lambda t: t[0]))
isAuto = False # we always start in a manual control mode
prevLine = 0
mode = ""
for line,modepair in orderedModes.iteritems():
    mode = modepair[0].upper()
    if prevLine == 0:
        prevLine = line
    if mode in autoModes:
        if not isAuto:
            manualSegments.append((prevLine,line-1))
            prevLine = line
        isAuto = True
    elif mode in manualModes:
        if isAuto:
            autoSegments.append((prevLine,line-1))
            prevLine = line
        isAuto = False
    elif mode in ignoreModes:
        if isAuto:
            autoSegments.append((prevLine,line-1))
        else:
            manualSegments.append((prevLine,line-1))
        prevLine = 0
    else:
        raise Exception("Unknown mode in TestPitchRollCoupling: %s" % mode)

# and handle the last segment, which doesn't have an ending
if mode in autoModes:
    autoSegments.append((prevLine,logdata.lineCount))
elif mode in manualModes:
    manualSegments.append((prevLine,logdata.lineCount))

print(len(autoSegments))
print(autoSegments)

# gps = logdata.channels["GPS"]
# gps_timeus = gps["TimeUS"].listData
# gps_lat = gps["Lat"].listData
#
# att = logdata.channels["ATT"]
# att_timeus = att["TimeUS"].listData
# att_roll = att["Roll"].listData
#
# gps1 = []
# att1 = []
#
# for i in range(len(gps_timeus)):
#     gps1.append({ 't': gps_timeus[i][1], 'lat': gps_lat[i][1] })
#
# for i in range(len(att_timeus)):
#     att1.append({ 't': att_timeus[i][1], 'roll': att_roll[i][1] })
#
# gps1.sort(key=lambda x: x['t'])
# att1.sort(key=lambda x: x['t'])
