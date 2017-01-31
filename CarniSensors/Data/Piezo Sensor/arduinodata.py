# coding=utf8

import serial
import csv
ser = serial.Serial('/dev/ttyACM4', 9600)#indicates which USB port to retrieve the data from
fichier = open('90%(3).csv', 'a')#open a file to add to
wr = csv.writer(fichier)
for i in range(2000): #choosing 2000 values to record in CSV file
    test = str(ser.readline()) #convert data to a string
    fichier.write(test) #writing data in the file
    print(test) #make data appear on terminal
fichier.close()

