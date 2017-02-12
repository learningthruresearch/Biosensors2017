import numpy as np
import matplotlib.pyplot as plt
import matplotlib
from math import *
import csv

Inten = [0,100]
allratio = []

def donnee(file):
    fichier = open(file, 'rb')                   # opens the file
    a = fichier.readlines()
    c = []
    for row in a:
        b = row.strip().split()
        c.append(float(b[1]))
    for i in range(0,len(c),2):
        p = c[i]/(c[i+1]+c[i])  # make a pourcentage of the total area that is above the line
        allratio.append(p)

donnee('Logcontrol.csv')

fig = plt.figure()
plt.plot(Inten, allratio, 'g+', mew=3, ms=10)   # mew = marker edge width, ms = marker size
plt.xlim(-2, 102)
plt.ylim(0, 1.1)
plt.title("Control: Fractal analysis ratio", size=23)
plt.xlabel("Intensity of LED (%)", size=23)
plt.ylabel("ratio", size=23)
#plt.show()
fig.savefig('fractalcontrol.png')
