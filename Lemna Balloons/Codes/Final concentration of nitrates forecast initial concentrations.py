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



with open('Tableau pre-csv - Concentration en nitrate.csv', 'rb') as csvfile: #Open the file
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


#------------------------------------Concentration 2-------------

with open('Tableau pre-csv - Concentration en nitrate.csv', 'rb') as csvfile: #Open the file
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

#------------------------------------Concentration 3--------------

with open('Tableau pre-csv - Concentration en nitrate.csv', 'rb') as csvfile: #Open the file
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



mean_E = []
mean_L = []
mean_C = []

for i in range(len(E1)):
     a = (E1[i] + E2[i] + E3[i]) / 3
     b = (L1[i] + L2[i] + L3[i]) / 3
     c = (C1[i] + C2[i] + C3[i]) / 3
     mean_E.append(a)
     mean_L.append(b)
     mean_C.append(c)
     

n_groups = 3
fig, ax = plt.subplots()

index = np.arange(n_groups)
bar_width = 0.3

opacity = 0.4
error_config = {'ecolor': '0.3'}

rects1 = plt.bar(index, mean_E, bar_width,
                 alpha=opacity,
                 color='b',
                 error_kw=error_config,
                 label='Experiment')

rects2 = plt.bar(index + bar_width, mean_L, bar_width,
                 alpha=opacity,
                 color='r',
                 error_kw=error_config,
                 label='L. minor')

rects3 = plt.bar(index + bar_width + bar_width, mean_C, bar_width,
                 alpha=opacity,
                 color='g',
                 error_kw=error_config,
                 label='C. reinhardtii')

plt.xlabel('Concentrations')
plt.ylabel('Final concentration of nitrates (mg.L-1)')
plt.title('Final concentration of nitrates forecast initial concentrations')
plt.xticks(index + bar_width + bar_width / 2, ('0 mg.L-1', '120 mg.L-1', '240 mg.L-1'))
plt.legend()

plt.tight_layout()
plt.show()

