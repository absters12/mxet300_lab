import numpy as np
import time
import L2_kinematics as kin
import L1_log as log

while (True):
    xdot = kin.getMotion()[0]
    thetadot = kin.getMotion()[1]

    pdl = kin.getPdCurrent()[0]
    pdr = kin.getPdCurrent()[1]

    log.tmpFile(pdl, "pdl.txt")
    log.tmpFile(pdr, "pdr.txt")


    print(f"xdot: {xdot:8.2f}     thetadot: {thetadot:8.2f}     pdl: {pdl:8.2f}     pdr: {pdr:8.2f}")

    time.sleep(0.2)