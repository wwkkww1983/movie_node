# Example of Raspi UPS Hat
#
# You should install wiringPi first.
# sudo apt-get update
# sudo apt-get upgrade
# git clone git://git.drogon.net/wiringPi
# cd wiringPi
# git pull origin
# cd wiringPi
# ./build

# We only provide 2 interfave to get battery information; 
#
#Interface 1:
#Function: get current battery voltage
#Return value: battery voltage;
#float getv();

#Interface 2:
#Function:    get battery capacity
#Return value: 0~100
#float getsoc(); 
#

import sys
# import Raspi UPS Hat library
import raspiupshat
import time
from datetime import datetime

# init Raspi UPS Hat
raspiupshat.init();

while True:
        # Get info
        print datetime.fromtimestamp(time.time())
        print "Voltage:%5.2fV" % raspiupshat.getv();
        print "Battery:%5i%%" % raspiupshat.getsoc();
        
        time.sleep(60)
        

