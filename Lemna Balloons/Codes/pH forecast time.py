
# coding: utf-8

# In[10]:

import numpy as np
import matplotlib.pyplot as plt
import matplotlib
from math import *
import csv

#------------------------------------Concentration 1--------------
time = []
E1 = [] #experiment: replicate 1
E2 = [] #replicate 2
E3 = [] #replicate 3
L1 = [] #control LEMNA: replicate 1
L2 = [] #replicate 2
L3 = [] #replicate 3
C1 = [] #control CHLAMYDOMONIA: replicate 1
C2 = [] #replicate 2
C3 = [] #replicate 3



with open('.csv', 'rb') as csvfile: #Open the file
    reader = csv.reader(csvfile) #read the file
    reader.next() #switch the first line
    reader.next() #switch the second line
    for row in reader:
        a = float(row[0]) #Takes the first argument of each line
        b = float(row[1]) #Takes the first argument of each line
        c = float(row[2])
        d = float(row[3])
        e = float(row[4])
        f = float(row[5])
        g = float(row[6])
        h = float(row[7])
        i = float(row[8])
        j = float(row[9])
        time.append(a) #Add the argument to the list
        E1.append(b)
        E2.append(c)
        E3.append(d)
        L1.append(e)
        L2.append(f)
        L3.append(g)
        C1.append(h)
        C2.append(i)
        C3.append(j)

plt.figure(figsize=(15, 6)) #Figure size
#matplotlib.style.use('ggplot') #Figule style

plt.plot(time, E1, color = "green")
plt.plot(time, E2, color = "green")
plt.plot(time, E3, color = "green")

plt.plot(time, L1, color = "blue")
plt.plot(time, L2, color = "blue")
plt.plot(time, L3, color = "blue")

plt.plot(time, C1, color = "red")
plt.plot(time, C2, color = "red")
plt.plot(time, C3, color = "red")
plt.xlabel("Time")
plt.ylabel("pH")
plt.title("Evolution of the pH forecast time for an initial nitrates  concentration of")

#------------------------------------Concentration 2--------------
time = []
E1 = [] #experiment: replicate 1
E2 = [] #replicate 2
E3 = [] #replicate 3
L1 = [] #control LEMNA: replicate 1
L2 = [] #replicate 2
L3 = [] #replicate 3
C1 = [] #control CHLAMYDOMONIA: replicate 1
C2 = [] #replicate 2
C3 = [] #replicate 3



with open('.csv', 'rb') as csvfile: #Open the file
    reader = csv.reader(csvfile) #read the file
    reader.next() #switch the first line
    reader.next() #switch the second line
    for row in reader:
        a = float(row[0]) #Takes the first argument of each line
        b = float(row[10]) #Takes the first argument of each line
        c = float(row[11])
        d = float(row[12])
        e = float(row[13])
        f = float(row[14])
        g = float(row[15])
        h = float(row[16])
        i = float(row[17])
        j = float(row[18])
        time.append(a) #Add the argument to the list
        E1.append(b)
        E2.append(c)
        E3.append(d)
        L1.append(e)
        L2.append(f)
        L3.append(g)
        C1.append(h)
        C2.append(i)
        C3.append(j)

plt.figure(figsize=(15, 6)) #Figure size
#matplotlib.style.use('ggplot') #Figule style

plt.plot(time, E1, color = "green")
plt.plot(time, E2, color = "green")
plt.plot(time, E3, color = "green")

plt.plot(time, L1, color = "blue")
plt.plot(time, L2, color = "blue")
plt.plot(time, L3, color = "blue")

plt.plot(time, C1, color = "red")
plt.plot(time, C2, color = "red")
plt.plot(time, C3, color = "red")
plt.xlabel("Time")
plt.ylabel("pH")
plt.title("Evolution of the pH forecast time for an initial nitrates  concentration of")

#------------------------------------Concentration 3--------------
time = []
E1 = [] #experiment: replicate 1
E2 = [] #replicate 2
E3 = [] #replicate 3
L1 = [] #control LEMNA: replicate 1
L2 = [] #replicate 2
L3 = [] #replicate 3
C1 = [] #control CHLAMYDOMONIA: replicate 1
C2 = [] #replicate 2
C3 = [] #replicate 3



with open('.csv', 'rb') as csvfile: #Open the file
    reader = csv.reader(csvfile) #read the file
    reader.next() #switch the first line
    reader.next() #switch the second line
    for row in reader:
        a = float(row[0]) #Takes the first argument of each line
        b = float(row[19]) #Takes the first argument of each line
        c = float(row[20])
        d = float(row[21])
        e = float(row[22])
        f = float(row[23])
        g = float(row[24])
        h = float(row[25])
        i = float(row[26])
        j = float(row[27])
        time.append(a) #Add the argument to the list
        E1.append(b)
        E2.append(c)
        E3.append(d)
        L1.append(e)
        L2.append(f)
        L3.append(g)
        C1.append(h)
        C2.append(i)
        C3.append(j)

plt.figure(figsize=(15, 6)) #Figure size
#matplotlib.style.use('ggplot') #Figule style

plt.plot(time, E1, color = "green")
plt.plot(time, E2, color = "green")
plt.plot(time, E3, color = "green")

plt.plot(time, L1, color = "blue")
plt.plot(time, L2, color = "blue")
plt.plot(time, L3, color = "blue")

plt.plot(time, C1, color = "red")
plt.plot(time, C2, color = "red")
plt.plot(time, C3, color = "red")
plt.xlabel("Time")
plt.ylabel("pH")
plt.title("Evolution of the pH forecast time for an initial nitrates  concentration of")

plt.show()




