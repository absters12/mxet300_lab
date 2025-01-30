from L1_ina import readVolts
import time
import L1_log as log

while True:
    voltage = readVolts()
    print(str(voltage) + "V")
    log.logArray([round(voltage, 2), 0])
    time.sleep(1)

