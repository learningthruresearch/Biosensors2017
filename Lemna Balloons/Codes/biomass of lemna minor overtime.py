# coding: utf-8

# In[10]:

import numpy as np
import matplotlib.pyplot as plt
import matplotlib
from math import *
import csv

initial_mass = []

with open('Tableau pre-csv - Biomasse des Lemna minor.csv', 'rb') as csvfile: #Open the file
    reader = csv.reader(csvfile) #read the file
    reader.next() #switch the first line
    for row in reader:
        a = row[0] #initial mass
        initial_mass.append(a)

print(initial_mass)
for i in range(len(initial_mass)):
    initial_mass[i] = float(initial_mass[i])

print(initial_mass)

plt.figure(figsize=(15, 6))
plt.boxplot([initial_mass])
plt.xlabel("Initial")
plt.ylabel("Biomass of Lemna minor (in mg +-0.1)")
plt.title("Biomass of Lemna minor overtime in function of their initial concentration of nitrates")
plt.show()
