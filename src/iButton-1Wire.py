#!/usr/bin/env python3

#-------------------------------------------------------------------
# iButons - iButton reader - 1-Wire interface 
#
# Purpose/Aim:
# This python3-program reads the Serial number of basic iButtons.
# Library/protocol used: 1-wire interface: the w1-gpio kernel on linux on the raspberry
#
# The 1-wire bus driver should be activated. 
# By default, the 1-wire kernel only reads the GPIO-4 every 10 seconds. 
# The reading time should be speeded-up to offer/have a better performance. ( w1_master_timeout=0, w1_master_timeout_us=500 )
# 
# @Date: 19-02-2019
# @Programmer: Ak. MT
#----------------------------------------------------------------


import os
import time
from datetime import datetime
import RPi.GPIO as GPIO
  
#os.system('modprobe wire timeout=0 timeout_us=500 slave_ttl=3')
os.system('modprobe w1-gpio')
os.system('modprobe w1-smem')
os.system('chmod a+w /sys/devices/w1_bus_master1/w1_master_slaves')
os.system('chmod a+w /sys/devices/w1_bus_master1/w1_master_remove')
os.system('chmod a+w /sys/devices/w1_bus_master1/w1_master_search')
base_dir = '/sys/devices/w1_bus_master1/w1_master_slaves'
delete_dir = '/sys/devices/w1_bus_master1/w1_master_remove'
   
def main():
  # Main program block

  while True:
  
    # iButton Read
    with open(base_dir, "r") as f:
        ID = f.read()
    if ID != 'not found.\n':
        print("{} : iButton-ID = {}".format(datetime.now().isoformat(), ID))
        #time.sleep(0.25)
        with open(delete_dir, "w") as d:
            d.write(ID)
    else:
        pass
        #print("Waiting") 
  
if __name__ == '__main__':
  
  try:
    main()
  except KeyboardInterrupt:
    pass
  finally:
    GPIO.cleanup()
