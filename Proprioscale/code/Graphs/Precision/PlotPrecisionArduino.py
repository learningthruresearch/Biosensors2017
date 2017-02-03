#!/usr/bin/env python
# -*- coding: utf-8 -*-

import matplotlib.pyplot as plt
import pylab

match = {4 : 300, 11: 300, 13: 300, 17: 300, 20: 300, 7 : 500, 14 : 500, 22: 500, 23: 500, 24: 500, 1 : 800, 12: 800, 16: 800, 18: 800, 19: 800, 2: 1000, 5: 1000, 9: 1000, 10: 1000, 15 : 1000, 3: 1300, 6 : 1300, 8 : 1300, 21 : 1300, 25 : 1300}

font = {'weight' : 'bold',
        'size'   : 25}
plt.rc('font', **font)

plt.ylabel('Variance of response')
plt.xlabel('Mass in gramme')
plt.title("Precision of FRS Arduino in function of different mass. n = 4")
#human
a = open("arduino.csv", "r")
human = []
for i in a:
	human.append(i.replace("\n", "").split(","))

number = 1
means = {300 : [], 500 : [], 800 : [], 1000 : [], 1300 : []}
tovariances = {300 : [], 500 : [], 800 : [], 1000 : [], 1300 : []}
variances = []
masses = []
for hu in human:
	means[match[int(hu[0])]] += [float(hu[2])]

for mass in means:
	mean = sum(means[mass]) / 5
	var = 0
	for value in means[mass]:
		var += (value - mean)**2
		if len(means[mass]) != 0:
			var = (1./float(len(means[mass]))) * var
			tovariances[mass] += [var]

print(tovariances)
means = {300 : [], 500 : [], 800 : [], 1000 : [], 1300 : []}
number = hu[0]
means[match[int(hu[0])]] += [float(hu[2])]
for val in tovariances:
	variances.append(tovariances[val])

print(variances)


box_leg = ['300', '500', '800', '1000', '1300']
#plt.boxplot(variances)
pylab.xticks([1,2,3,4,5], box_leg)

plt.show()