# coding = UTF-8
# written by Samuel Churlaud
# see github.com/learningthruresearch/Biosensors2017/tree/master/poworm_rangers

import serial
import time

ser = serial.Serial('/dev/ttyACM0', 9600)
output = open('data_output', 'w+')
for i in range(100):
    data = ser.readline()
    output.write(data)
    time.sleep(0.1)
