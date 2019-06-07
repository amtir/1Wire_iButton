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
    f = open(base_dir, "r")
    ID = f.read()
    f.close()
    if ID != 'not found.\n':
        print("{} : iButton-ID = {}".format(datetime.now().isoformat(), ID))
        #time.sleep(0.25)
        d = open(delete_dir, "w")
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



'''

pi@raspberrypi:~/iButton-1Wire $ 
pi@raspberrypi:~/iButton-1Wire $ sudo python3 iButton-1Wire.py 
2019-06-07T16:45:15.076385 : iButton-ID = 01-00001933801c

2019-06-07T16:45:15.077992 : iButton-ID = 01-00001933801c

2019-06-07T16:45:15.135908 : iButton-ID = 01-00001933801c

2019-06-07T16:45:15.195751 : iButton-ID = 01-00001933801c

2019-06-07T16:45:15.255419 : iButton-ID = 01-00001933801c

2019-06-07T16:45:15.315571 : iButton-ID = 01-00001933801c

2019-06-07T16:45:15.375553 : iButton-ID = 01-00001933801c

2019-06-07T16:45:15.465508 : iButton-ID = 01-00001933801c

2019-06-07T16:45:15.525526 : iButton-ID = 01-00001933801c

2019-06-07T16:45:15.585670 : iButton-ID = 01-00001933801c

2019-06-07T16:45:15.645559 : iButton-ID = 01-00001933801c

2019-06-07T16:45:15.705490 : iButton-ID = 01-00001933801c



2019-06-07T16:45:21.795714 : iButton-ID = 01-00000fcfae14

2019-06-07T16:45:21.796982 : iButton-ID = 01-00000fcfae14

2019-06-07T16:45:21.855697 : iButton-ID = 01-00000fcfae14

2019-06-07T16:45:21.915688 : iButton-ID = 01-00000fcfae14

2019-06-07T16:45:21.985695 : iButton-ID = 01-00000fcfae14

2019-06-07T16:45:22.045503 : iButton-ID = 01-00000fcfae14

2019-06-07T16:45:22.105439 : iButton-ID = 01-00000fcfae14

2019-06-07T16:45:22.165781 : iButton-ID = 01-00000fcfae14





'''






