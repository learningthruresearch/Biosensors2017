import numpy as np
import matplotlib.pyplot as plt
import matplotlib
from math import *
import csv

Inten = [0, 0, 0, 20, 20, 20, 40, 40, 40, 60, 60, 60, 80, 80, 80, 100, 100, 100]
allratio = []

def donnee(file):

	a = []
	data = file
	with open(data, 'rb') as csvfile: #Open the file
		reader = csv.reader(csvfile)
		reader.next() #switch the first line
		for row in reader:
			b=row[6]
			allratio.append(float(b))
	print(allratio)

donnee('Result1.csv')
donnee('Result2.csv')
donnee('Result3.csv')
donnee('Result4.csv')
donnee('Result5.csv')
donnee('Result6.csv')
print(allratio)


fig = plt.figure()
plt.plot(Inten, allratio, 'rx')
plt.xlim(-2, 102)
plt.title("Development towards light or gravity in function of the intensity of light")
plt.xlabel("Intensity of LED (%)")
plt.ylabel("maximum distance to line (mm)")
fig.savefig('Test2.png')
