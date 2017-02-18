#!/usr/bin/env python
# -*- coding: utf-8 -*-

import matplotlib.pyplot as plt

names = ["00_1.csv", "00_2.csv", "00_3.csv", "0003_1.csv", "0003_2.csv", "0003_3.csv", "0003_4.csv","0005_1.csv", "0005_2.csv", "0005_3.csv", "0008_1.csv", "0008_2.csv", "0008_3.csv",  "002_1.csv", "002_2.csv", "002_3.csv", "002_4.csv", "003_1.csv", "003_2.csv", "01_1.csv", "01_2.csv", "01_3.csv"]
conversion = {3.5 : 24.5}
toploty = []
toplotx = []
datum = {}
every = {}
for name in names:
	datum[str(name.split("_")[0][0]+ "." + name.split("_")[0][1:])] = []
for name in names:
	every[str(name.split("_")[0][0]+ "." + name.split("_")[0][1:])] = []

for name in names:
	numero = []
	distance = []
	numeros = []
	distances = []
	a = open(name, "r")
	print(name)
	tic = 1
	for i in a:
		data = i.split(",")
		if tic == 1:
			num = data[1]
			tic = 2
		if data[1] != num:
			numeros.append(numero)
			distances.append(distance)
			numero = []
			distance = []
			vitesse = []
			#numero.append(abs(float(data[1])))
			#distance.append(abs(float(data[5])))
			num = data[1]
		else:
			numero.append(abs(float(data[1])))
			distance.append(abs(float(data[5])))
	numeros.append(numero)
	distances.append(distance)

	dist = 0
	for volvox in distances:
		dist += sum(volvox)
		dist2 = (sum(volvox) * 3.5) / 24.5
		every[str(name.split("_")[0][0]+ "." + name.split("_")[0][1:])] = every[str(name.split("_")[0][0]+ "." + name.split("_")[0][1:])] + [dist2]

	dist = dist/len(distances)
	dist = (dist * 3.5) / 24.5
	toploty.append(dist)
	toplotx.append(float(name.split("_")[0][0]+ "." + name.split("_")[0][1:]))
	datum[str(name.split("_")[0][0]+ "." + name.split("_")[0][1:])] = datum[str(name.split("_")[0][0] + "." + name.split("_")[0][1:])] + [dist]

print(every)
unx = []
uny = []
for i in every:
	for j in every[i]:
		python = "cool"
		#plt.plot(i, j, "o", color="blue")
	#plt.plot(i, sum(every[i] )/ len(every[i]), "o", color="red", markersize=22)
	unx.append(i)
	uny.append(sum(datum[i])/len(datum[i]))
#plt.plot(unx, uny)

font = {'weight' : 'bold',
        'size'   : 25}
plt.rc('font', **font)

plt.ylabel('Distance in mm')
plt.xlabel('salt concentration g/ml')
plt.title("Volvox movement in function of the salinity of water")
plt.show()