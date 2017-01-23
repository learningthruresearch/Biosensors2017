import serial                                                                                      
#Data output from Arduino

import csv                                                                                         
#used to manipulate .csv files

ser = serial.Serial('/dev/ttyACM0', 2000000, timeout=2, xonxoff=False, rtscts=False, dsrdtr=False) 
#associates the serial from arduino to a variable       
                                                                
ser.flushInput()
ser.flushOutput()
myfile = open('data_output.csv', 'a') 
#creates a csv file

wr = csv.writer(myfile, quoting=csv.QUOTE_ALL)                                                     
#associate a variable to write into that csv file

mylist=[]
for i in range(30):
  data_raw = ser.readline()
  #reads line by line the csv file and stocks it in lists
  
  print(data_raw)
  mylist.append(data_raw)
wr.writerow(mylist)
print("Hello World")

