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

#Rough data
LDR = [0.4736842105, 201.8947368, 276.8947368, 844.5789474, 811.7368421, 945.3684211, 929.5789474, 967.9473684]
luxmeter = [0.003, 0.007, 0.104, 0.5, 1] 
lightss = [0, 2, 5, 8, 10] # intensity of the microscope light
lights = [0, 2, 2, 5, 5, 8, 8, 10] # intensity of the microscope light for duplicate


#normalize the LDR output value
normLDR = []
for i in LDR:
	a = (i * 1)/(967.9473684) #noramalize between 0 and 1
	print(a)
	print(i)
	normLDR.append(a)


#Making the graph
red_patch = mpatches.Patch(color='red', label='Lux meter')
green_patch = mpatches.Patch(color='blue', label='Arduino Output')        # legend
plt.legend(handles=[red_patch], loc='upper left')
plt.plot(lightss, luxmeter, "o", color="red", markersize=18)              # curve
plt.plot(lights, normLDR, "^", color="blue", markersize=18)
plt.xlim(xmin=-1)
plt.xlim(xmax=11)                    # set size of the graph
plt.ylim(ymin=-0.2)
plt.ylim(ymax=1.2)
plt.ylabel('Normalized scale')
plt.xlabel('light intensity calibration by microscope')
plt.title("Comparison in normalized scale between \n Arduino output and lux meter filter 3")
plt.show()