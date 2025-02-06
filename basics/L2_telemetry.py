from L1_ina import readVolts
import time
import L1_log as log

def voltage_val():
    voltage = readVolts()
    print(str(voltage) + "V")
    log.tmpFile(direction, "voltage_value.txt")
    time.sleep(1)

