import numpy as np
import matplotlib.pyplot as plt
import matplotlib
from math import *
import csv

Inten = [0, 0, 0, 20, 20, 20, 40, 40, 40, 60, 60, 60, 80, 80, 80, 100, 100, 100]
allratio = []

def donnee(file):

	a = []
	ratios = []
	data = file
	with open(data, 'rb') as csvfile: #Open the file
		reader = csv.reader(csvfile)
		reader.next() #switch the first line
		for row in reader:
			b=row[1]
			a.append(float(b))
		p1 = a[0]/(a[1]+a[0])    #if A = 0 and if B = 0
		p2 = a[2]/(a[3]+a[2])
		p3 = a[4]/(a[5]+a[4])
	allratio.append(p1)
	allratio.append(p2)
	allratio.append(p3)

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
