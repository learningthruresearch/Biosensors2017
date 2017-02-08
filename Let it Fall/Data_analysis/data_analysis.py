import numpy as np
import matplotlib.pyplot as plt
import matplotlib
from math import *
import csv

a = []

with open('Results.csv', 'rb') as csvfile: #Open the file
	reader = csv.reader(csvfile)
	reader.next() #switch the first line
	for row in reader:
		b=row[0]
		a.append(float(b))
print(a)



"""
fig = plt.figure()
plt.boxplot(normef)
plt.xticks([1, 2, 3, 4, 5, 6, 7, 8, 9 , 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20],['0', '1', '2', '3', '4', '5', '6', '7', '8','9', '10' , '11' , '12' , '13' , '14' , '15' , '16' , '17' , '18' , '19', '20'])
plt.title("Sensitivity of a magnetometer in function of the amplitude")
plt.xlabel("amplitude (V)")
plt.ylabel("value sensed(a.u.)")
fig.savefig('champele.png')"""
