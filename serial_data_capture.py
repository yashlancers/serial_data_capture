import time
import os

# sudoPassword = 'mypass'
t = time.strftime('%Y-%m-%d-Time-%H-%M', time.localtime(time.time()))
command = 'minicom -D /dev/ttyUSB0 -C /home/pi/serial_data_capture/csvData/csvDate'+ t +'.csv'
# p = os.system('echo %s|sudo -S %s' % (sudoPassword, command))
p = os.system('sudo %s' % (command))