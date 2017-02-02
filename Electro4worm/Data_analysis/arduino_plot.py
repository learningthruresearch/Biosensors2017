import serial                                                                                      
#Data output from Arduino

import csv                                                                                         
#used to manipulate .csv files
import numpy as np
import matplotlib.pyplot as plt
import math as m

normef = []
def donnee(file):

	data = file
	myfile = open(data, 'r')
	b = myfile.readlines()

	x=[]
	y=[]
	z=[]
	norme = []
	i = 0
	for a in b:
		a = a.split(',')
		x.append(int(a[0]))
		y.append(int(a[1]))
		z.append(int(a[2]))
		norme.append(m.sqrt(x[i]**2 + y[i]**2 + z[i]**2))
		i += 1
	normef.append(norme)

donnee('A0.csv')
donnee('A1.csv')
donnee('A2.csv')
donnee('A3.csv')
donnee('A4.csv')
donnee('A5.csv')
donnee('A6.csv')
donnee('A7.csv')
donnee('A8.csv')
donnee('A9.csv')
donnee('A10.csv')
donnee('A11.csv')
donnee('A12.csv')
donnee('A13.csv')
donnee('A14.csv')
donnee('A15.csv')
donnee('A16.csv')
donnee('A17.csv')
donnee('A18.csv')

fig = plt.figure()
plt.boxplot(normef)
plt.xticks([1, 2, 3, 4, 5, 6, 7, 8, 9 , 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20],['0', '1', '2', '3', '4', '5', '6', '7', '8','9', '10' , '11' , '12' , '13' , '14' , '15' , '16' , '17' , '18' , '19', '20'])
plt.title("Sensitivity of a magnetometer in function of the amplitude")
plt.xlabel("amplitude (V)")
plt.ylabel("value sensed(a.u.)")
fig.savefig('champele.png')
