import serial
import csv

ser = serial.Serial('/dev/ttyACM0', 9600)
data = open("../Lum255/sensor10_255_2.csv", "a")
write = csv.writer(data)
while True :
    line = str(ser.readline())
    data.write(line[2:-3]+'\n')
    print(line[2:-3])
data.close()

