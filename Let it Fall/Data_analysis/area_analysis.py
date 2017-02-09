import numpy as np
import matplotlib.pyplot as plt
import matplotlib
from math import *
import csv

# Execute this program with Python2

Inten = [0, 0, 0, 20, 20, 20, 40, 40, 40, 60, 60, 60, 80, 80, 80, 100, 100, 100]
allratio = []

def donnee(file):

	a = []
	with open(file, 'rb') as csvfile: #Open the file
		reader = csv.reader(csvfile)
		reader.next() #switch the first line
		for row in reader:
			b=row[1]
			a.append(float(b))
        for i in range(0,6,2):
            if i < 1:
                p = 0
            else:
                p = a[i]/(a[i+1]+a[i])
            allratio.append(p)

donnee('Results.csv')
donnee('Results1.csv')
donnee('Results2.csv')
donnee('Results3.csv')
donnee('Results4.csv')
donnee('Results5.csv')


#fig = plt.figure()
plt.plot(Inten, allratio, 'g+', mew=3, ms=10)
plt.xlim(-2, 102)
plt.ylim(0, 1.1)
plt.title("Development towards light or gravity in function of the intensity of light", size=23)
plt.xlabel("Intensity of LED (%)", size=23)
plt.ylabel("ratio", size=23)
plt.show()
#fig.savefig('Test1.png')
