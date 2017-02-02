import serial                                                                                      
#Data output from Arduino

import csv                                                                                         
#used to manipulate .csv files
import numpy as np
import matplotlib.pyplot as plt
import math as m

ser = serial.Serial('/dev/ttyACM2', 38400)      
myfile = open('a0.csv', 'a') 
write = csv.writer(myfile)
for i in range(100):
    line = str(ser.readline())
    myfile.write(line[2:-5]+'\n')
myfile.close()