import time
import L1_log as log
from L2_compass_heading import get_heading


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


while True:
    heading = get_heading()
    print(str(heading) + " degrees")
    log.logArray([0 ,round(heading, 2)])
    cardinal(heading)

    time.sleep(1)
