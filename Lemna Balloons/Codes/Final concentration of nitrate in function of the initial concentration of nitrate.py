#Final concentration of nitrates in function of the initial concentration of nitrates

# coding: utf-8

# In[10]:

import numpy as np
import matplotlib.pyplot as plt
import matplotlib
from math import *
import csv
#------------------------------------Concentration 1--------------
E1 = [] #experiment: replicate 1
E2 = [] #replicate 2
E3 = [] #replicate 3
C1 = [] #control CHLAMYDOMONIA: replicate 1
C2 = [] #replicate 2
C3 = [] #replicate 3



#------------------------------------Concentration 1--------------
with open('Tableau pre-csv - Alice - Graph 1.csv', 'rb') as csvfile: #Open the file
    reader = csv.reader(csvfile) #read the file
    reader.next() #switch the first line
    reader.next() #switch the second line
    for row in reader:
        b = float(row[1]) #Takes the first argument of each line
        c = float(row[2])
        d = float(row[3])
        e = float(row[4])
        f = float(row[5])
        g = float(row[6])
        E1.append(b)
        E2.append(c)
        E3.append(d)
        C1.append(e)
        C2.append(f)
        C3.append(g)

#------------------------------------Concentration 2--------------
with open('Tableau pre-csv - Alice - Graph 1.csv', 'rb') as csvfile: #Open the file
    reader = csv.reader(csvfile) #read the file
    reader.next() #switch the first line
    reader.next() #switch the second line
    for row in reader:
        b = float(row[7]) #Takes the first argument of each line
        c = float(row[8])
        d = float(row[9])
        e = float(row[10])
        f = float(row[11])
        g = float(row[12])
        E1.append(b)
        E2.append(c)
        E3.append(d)
        C1.append(e)
        C2.append(f)
        C3.append(g)

#------------------------------------Concentration 3--------------
with open('Tableau pre-csv - Alice - Graph 1.csv', 'rb') as csvfile: #Open the file
    reader = csv.reader(csvfile) #read the file
    reader.next() #switch the first line
    reader.next() #switch the second line
    for row in reader:
        b = float(row[13]) #Takes the first argument of each line
        c = float(row[14])
        d = float(row[15])
        e = float(row[16])
        f = float(row[17])
        g = float(row[18])
        E1.append(b)
        E2.append(c)
        E3.append(d)
        C1.append(e)
        C2.append(f)
        C3.append(g)


A = [1, 2, 3]

plt.figure(figsize=(15, 6)) #Figure size
#matplotlib.style.use('ggplot') #Figule style

plt.plot(A, E1, 'o', color = "green")
plt.plot(A, E2, 'o', color = "green")
plt.plot(A, E3, 'o', color = "green")


plt.plot(A, C1, 'o', color = "red")
plt.plot(A, C2, 'o', color = "red")
plt.plot(A, C3, 'o', color = "red")
plt.xlabel("Concentrations")
plt.ylabel("Final concentration of nitrates")
plt.title("Final concentration of nitrates in function of the initial concentration of nitrate")
plt.show()
