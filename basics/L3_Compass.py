import time
import L1_log as log
from L2_compass_heading import get_heading
from L2_telemetry import voltage_val

def cardinal(heading):
    if -22.5 <= heading <= 22.5:
        direction = "North"
    elif 22.5 < heading <= 67.5:
        direction = "North East"
    elif 67.5 < heading <= 112.5:
        direction = "East"
    elif 112.5 < heading <= 157.5:
        direction = "South East"
    elif 157.5 < heading <= 180 or -180 <= heading <= -157.5:
        direction = "South"
    elif -157.5 < heading <= -112.5:
        direction = "South West"
    elif -112.5 < heading <= -67.5:
        direction = "West"
    elif -67.5 < heading <= -22.5:
        direction = "North West"
    else:
        direction = "Unknown"

    print(direction)
    log.stringTmpFile(direction, "compass_direction.txt")
    log.tmpFile(heading, "compass_direction_val.txt")


while True:
    heading = get_heading()
    print(str(heading) + " degrees")
    cardinal(heading)
    time.sleep(1)
