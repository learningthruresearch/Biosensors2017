# coding: utf-8

# In[10]:

import numpy as np
import matplotlib.pyplot as plt
import matplotlib
from math import *
import csv

#------------------------------------Concentration 1--------------
day1 = []
day2 = []
day3 = []
day4 = []

with open('Tableau pre-csv - Concentration initiale algues.csv', 'rb') as csvfile: #Open the file
    reader = csv.reader(csvfile) #read the file
    reader.next() #switch the first line
    reader.next() #switch the second line
    for row in reader:
        a = row[1] #DAY 1
        day1.append(a)

day1 = day1[:73]

for i in range(len(day1)):
    day1[i] = float(day1[i])

print(day1)

plt.figure(figsize=(15, 6))
plt.boxplot([day1])
plt.xlabel("Measurements over time")
plt.ylabel("Concentration of living algae")
plt.show()
