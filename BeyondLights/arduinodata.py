# coding=utf8

import serial
import csv
ser = serial.Serial('/dev/ttyACM2', 9600)
fichier = open('control.csv', 'a')
wr = csv.writer(fichier)
for i in range(700):
    test = str(ser.readline())
    fichier.write(test)
    print(test)
fichier.close()

