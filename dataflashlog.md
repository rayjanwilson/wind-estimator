data flash needs

- EKF1
    - TimeMS - time in msec from startup
        - need to sync with gps time
    - Roll
        - angle in deg
    - Pitch
        - angle in deg
    - Yaw
        - angle in degrees
    - VN,VE,VD
        – North,East,Down velocities (m/s)
- ATT (attitude information)
    - RollIn: the pilot’s desired roll angle in centi-degrees (roll left is negative, right is positive)
    - Roll: the vehicle’s actual roll in centi-degrees (roll left is negative, right is positive)
    - PitchIn: the pilot’s desired pitch angle in centi-degrees (pitch forward is negative, pitch back is positive)
    - Pitch: the vehicle’s actual pitch angle in centi-degrees (roll left is negative, right is positive)
    - YawIn: the pilot’s desired yaw rate as a number from -4500 ~ 4500 (not in deg/sec, clockwise is positive)
    - Yaw: the vehicles actual heading in centi-degrees with 0 = north
    - NavYaw: the desired heading in centi-degrees
- CTUN (throttle and altitude information):
    - ThrIn: the pilot’s throttle in as a number from 0 to 1000
    - SonAlt: the altitude above ground according to the sonar
    - BarAlt: the altitude above ground according to the barometer
    - WPAlt: the desired altitude while in AltHold, Loiter, RTL or Auto flight modes
    - NavThr: not used
    - AngBst: throttle increase (from 0 ~ 1000) as a result of the copter leaning over (automatically added to all pilot and autopilot throttle to reduce altitude loss while leaning)
    - CRate: accelerometer + baro climb rate estimate in cm/s
    - ThrOut: final throttle output sent to the motors (from 0 ~ 1000). Normally equal to ThrIn+AngBst while in stabilize mode.
    - DCRate – pilot desired climb rate in cm/s
- CURRENT (battery voltage, current and board voltage information):
    - Thr: pilot input throttle from 0 ~ 1000
    - ThrInt: integrated throttle (i.e. sum of total throttle output for this flight)
    - Volt: battery voltage in volts * 100
    - Curr: current drawn from the battery in amps * 100
    - Vcc: board voltage
    - CurrTot: total current drawn from battery
- GPS
    - Status – 0 = no GPS, 1 = GPS but no fix, 2 = GPS with 2D fix, 3 = GPS with 3D fix
    - Time: the GPS reported time since epoch in milliseconds
    - NSats: the number of satellites current being used
    - HDop: a measure of gps precision (1.5 is good, >2.0 is not so good)
    - Lat: Lattitude according to the GPS
    - Lng: Longitude according to the GPS
    - RelAlt: Accelerometer + Baro altitude in meters
    - Alt: GPS reported altitude (not used by the flight controller)
    - SPD: horizontal ground speed in m/s
    - GCrs: ground course in degrees (0 = north)
- Mode (flight mode):
    - Mode: the flight mode displayed as a string (i.e. STABILIZE, LOITER, etc)
    - ThrCrs: throttle cruise (from 0 ~ 1000) which is the autopilot’s best guess as to what throttle is required to maintain a stable hover
- RCOUT

GPS Labels:  ['TimeUS', 'Status', 'GMS', 'GWk', 'NSats', 'HDop', 'Lat', 'Lng', 'RAlt', 'Alt', 'Spd', 'GCrs', 'VZ']
EKF1 Labels:  ['TimeUS', 'Roll', 'Pitch', 'Yaw', 'VN', 'VE', 'VD', 'PN', 'PE', 'PD', 'GX', 'GY', 'GZ']

GPS, time_us, status, gps_week_ms, gps week, num_sats, hdop, latitude, longitude, altitude, ground_speed, ground_course, vel_z
GPS, 90677253, 3, 501201000, 1853, 12, 1.73, 64.8540366, -147.8592679, 0.00, 147.21, 0.14, 0.00, 0.34

toUnixTime(gps_week_ms, gps_week_number){
    return gps_week_ms/1000 + gps_week_number * 60 * 60 * 24 * 7
}
