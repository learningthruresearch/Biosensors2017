#!/usr/bin/env python
# -*- coding: utf-8 -*-

#Packages needed
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
import pylab as pltt

#definition of the label size
font = {'weight' : 'bold',
        'size'   : 25}
plt.rc('font', **font)

#Parcing
a = open("Raw.csv", "r") #open the datafile
distances = [] #keep all the distances
numeros = [] #keep all the name of the chloroplasts
light = [] #keep the intensity of the light
vitesses = [] #keep all the velocities
temps = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10] #time in minutes
lights = [0, 1, 1, 2, 2, 3, 3, 4] # intensity negativControl
label = [4, 5, 5, 25, 25, 127, 127, 249]
numero = []
distance = []
vitesse = []
light = 0
moy_distances = []
for i in a:
	data = i.split(",")
	moy_distance = []

	if data[0] == "":
		light += 1
		moy_distances.append(sum(distance)/len(distance))
		numero = []
		distance = []
		vitesse = []
	elif float(data[1]) == 1:
		coucou = "busous"
	else:
		numero.append(data[0])
		distance.append(((float(data[2]))**2)**(0.5))
		vitesse.append(data[3])
moy_distances.append(sum(distance)/len(distance))

red_patch = mpatches.Patch(color='red', label='Controls')
blue_patch = mpatches.Patch(color='blue', label='Light intensity')
plt.legend(handles=[red_patch, blue_patch], loc='upper left')
plt.plot([0, 4], [moy_distances[0], moy_distances[-1]], "o", color="red", markersize=12)
plt.plot(lights[1:-1], moy_distances[1:-1], "o", color="blue", markersize=12)
plt.xlim(xmin=-1)
plt.xlim(xmax=5)
plt.ylim(ymin=0)
plt.ylim(ymax=1)
pltt.xticks(lights, label)
pltt.tight_layout(pad=1.08, h_pad=10.08, w_pad=None, rect=None)
plt.ylabel('Mouvement in micrometer')
plt.xlabel('light intensity in lux')
plt.title("Mean of chloroplasts movement in function of light intensity in Egeria densa")
plt.show()