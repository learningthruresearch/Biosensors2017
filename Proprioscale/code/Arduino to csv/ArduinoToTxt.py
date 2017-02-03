#from http://www.instructables.com/id/Using-an-Arduino-and-Python-to-plotsave-data/step3/Python-code/
#http://stackoverflow.com/questions/24214643/python-to-automatically-select-serial-ports-for-arduino

import serial
import matplotlib.pyplot as plt
import numpy as np

import warnings
import serial.tools.list_ports

arduino_ports = [
    p.device
    for p in serial.tools.list_ports.comports()
    if 'Arduino' in p.description
]
if not arduino_ports:
    raise IOError("No Arduino found")
if len(arduino_ports) > 1:
    warnings.warn('Multiple Arduinos found - using the first')

ser = serial.Serial(arduino_ports[0])

#ser = serial.Serial(comPort, 9600) #sets up serial connection (make sure baud rate is correct - matches Arduino)
connected = False

while not connected:
    serin = ser.read()
    connected = True


plt.ion()                    #sets plot to animation mode

length = 300                #determines length of data taking session (in data points)
x = [0]*length               #create empty variable of length of test
#y = [0]*length

xline, = plt.plot(x)         #sets up future lines to be modified
#yline, = plt.plot(y)
plt.ylim(0,1500)        #sets the y axis limits

time = 0
for i in range(length):     #while you are taking data
    data = ser.readline()    #reads until it gets a carriage return. MAKE SURE THERE IS A CARRIAGE RETURN OR IT READS FOREVER
    sep = data.split()      #splits string into a list at the tabs
    print sep

    if len(sep) != 0:
    	x.append(int(sep[0]))
    	#y.append(int(time))
    	time += 200
    	del x[0]
    	#del y[0]
    	xline.set_xdata(np.arange(len(x))) #sets xdata to new list length
    	#yline.set_xdata(np.arange(len(y)))
    	xline.set_ydata(x)                 #sets ydata to new list
    	#yline.set_ydata(y)
    	plt.pause(0.001)                   #in seconds
    	plt.draw()                         #draws new plot


rows = zip(x)                  #combines lists together
np.savetxt("data25", x)
#row_arr = np.array(rows)               #creates array from list
#np.savetxt("result", row_arr) #save data in file (load w/np.loadtxt())

ser.close() #closes serial connection (very important to do this! if you have an error partway through the code, type this into the cmd line to close the connection)