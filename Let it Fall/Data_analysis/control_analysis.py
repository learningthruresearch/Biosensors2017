import numpy as np
import matplotlib.pyplot as plt
import matplotlib
from math import *
import csv

# Execute this program with Python2

Inten = [0, 0, 0, 100, 100, 100]
allratio = []

def donnee(file):

	a = []
	with open(file, 'rb') as csvfile: # Open the file
		reader = csv.reader(csvfile)
		reader.next()                 # Switch the first line
		for row in reader:
			b=row[1]                  # Take the second row
			a.append(float(b))        # Converts itin a float
        for i in range(0,6,2):        # Iterates on the pair numbers between 0 and 6: 0, 2, 4
            if i < 1:                 # If there's no area above or below the line
                p = 0                 # make the ratio equal to zero
            else:
                p = a[i]/(a[i+1]+a[i])  # make a pourcentage of the total area that is above the line
            allratio.append(p)

donnee('Results.csv')
donnee('Results1.csv')


#fig = plt.figure()
plt.plot(Inten, allratio, 'g+', mew=3, ms=10)   # mew = marker edge width, ms = marker size
plt.xlim(-2, 102)
plt.ylim(0, 1.1)
plt.title("Controls: Development towards light or gravity in function of the intensity of light", size=23)
plt.xlabel("Intensity of LED (%)", size=23)
plt.ylabel("ratio", size=23)
plt.show()
#fig.savefig('Test1.png')
