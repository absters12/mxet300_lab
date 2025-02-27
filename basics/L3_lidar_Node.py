import numpy as np
import time
import L1_lidar as lidar
import L2_vector as vector
import L1_log as log

while(1):
    nearest_vector = vector.getNearest()    # Get the closest object [distance, angle]
    dist = nearest_vector[0]                # Extract distance
    angle = nearest_vector[1]               # Extract angle

    cart_coords = vector.polar2cart(dist, angle)
    x = cart_coords[0]
    y = cart_coords[1]

    log.tmpFile(dist, "lidar_dist.txt")
    log.tmpFile(angle, "lidar_angle.txt")
    log.tmpFile(x, "lidar_x.txt")
    log.tmpFile(y, "lidar_y.txt")